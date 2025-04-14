export default {
    build: {
      outDir: '../static/js',
      emptyOutDir: true,
      rollupOptions: {
        input: './main.js',
        output: {
          entryFileNames: 'bundle.js',
        }
      }
    }
  }
  