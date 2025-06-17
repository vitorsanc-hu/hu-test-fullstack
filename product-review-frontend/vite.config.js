import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      // Proxy para API Flask
      '/produtos': 'http://localhost:8000',
      '/avaliacoes': 'http://localhost:8000'
    }
  }
})
