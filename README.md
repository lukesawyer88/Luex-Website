# Luex website

Marketing site for Luex (luexgroup.com). Built with Astro (static pages, fast, good for SEO).

## Where to edit

- `src/data/pricing.json` – every price. All pages read from here.
- `src/data/modules.json` – the module list. Counts and app pages follow it.
- `src/data/site.json` – name, domain, tagline, launch date.

Prices and modules are placeholders until the `placeholder` flag in pricing.json is removed.

## Commands

```
npm install
npm run dev      # local preview
npm run build    # checks the data files, then builds to dist/
```

`npm run check` validates the two data files and runs automatically before each build.

## Deploy

Planned: Cloudflare Pages, build command `npm run build`, output folder `dist`.

## Rules

- Do not touch the luex-app repo or the Luex App Supabase project from here.
- Only describe modules on the site once their status in modules.json is `built`.
