import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://www.luexgroup.com',
  trailingSlash: 'never',
  build: { format: 'directory' },
});
