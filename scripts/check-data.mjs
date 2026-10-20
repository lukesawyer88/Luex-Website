// Runs before every build. Catches typos in the two editable data files.
import { readFileSync } from 'node:fs';

const load = (p) => JSON.parse(readFileSync(new URL(p, import.meta.url), 'utf8'));
const errors = [];

let modules, pricing;
try { modules = load('../src/data/modules.json').modules; } catch (e) { errors.push('modules.json is not valid JSON: ' + e.message); }
try { pricing = load('../src/data/pricing.json'); } catch (e) { errors.push('pricing.json is not valid JSON: ' + e.message); }

if (modules) {
  const seen = new Set();
  for (const m of modules) {
    if (!m.slug || !m.name || !m.group) errors.push(`Module missing slug, name or group: ${JSON.stringify(m)}`);
    if (seen.has(m.slug)) errors.push(`Duplicate module slug: ${m.slug}`);
    seen.add(m.slug);
    if (!['built', 'building', 'planned'].includes(m.status)) errors.push(`${m.slug}: status must be built, building or planned`);
  }
}

if (pricing) {
  const bands = pricing.singleApp?.bands ?? [];
  if (!bands.length) errors.push('pricing.json: no single-app bands');
  bands.forEach((b, i) => {
    if (typeof b.pricePerMonth !== 'number') errors.push(`Band "${b.label}": pricePerMonth must be a number`);
    if (i > 0 && b.minUsers !== bands[i - 1].maxUsers + 1) errors.push(`Band "${b.label}" does not follow on from the previous band`);
  });
  for (const k of ['basePricePerMonth', 'usersIncluded', 'extraFullUserPerMonth', 'extraLightUserPerMonth']) {
    if (typeof pricing.hub?.[k] !== 'number') errors.push(`pricing.json: hub.${k} must be a number`);
  }
}

if (errors.length) {
  console.error('\nData check failed:\n - ' + errors.join('\n - ') + '\n');
  process.exit(1);
}
console.log(`Data check passed: ${modules.length} modules, ${pricing.singleApp.bands.length} single-app bands.`);
