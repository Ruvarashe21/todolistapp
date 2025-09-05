
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5174, // frontend port
    hmr: {
      clientPort: 5174, // force websocket to connect to correct port
    },
  },
})

