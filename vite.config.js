import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [tailwindcss()],
  build: {
    outDir: 'static/dist', 
    rollupOptions: {
      input: 'static/src/main.css', 
    }
  }
})