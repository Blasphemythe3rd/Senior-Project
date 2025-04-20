import {
    Chart,
    CategoryScale,
    LinearScale,
    BarController,
    BarElement,
  } from 'chart.js';
  
  import { BoxPlotController, ViolinController} from '@sgratzl/chartjs-chart-boxplot';
  
  // Register Chart.js + the boxplot plugin components
  Chart.register(
    CategoryScale,
    LinearScale,
    BarController,
    BarElement,
    BoxPlotController,
    ViolinController
  );
  
  // Sample boxplot data
  const ctx = document.getElementById('myChart').getContext('2d');
  const chart = new Chart(ctx, {
    type: 'boxplot',
    data: {
      labels: ['Group 1', 'Group 2'],
      datasets: [{
        label: 'Latency (ms)',
        backgroundColor: 'rgba(255,99,132,0.5)',
        borderColor: 'rgba(255,99,132,1)',
        borderWidth: 1,
        outlierColor: '#999999',
        padding: 10,
        itemRadius: 0,
        data: [
          [100, 200, 300, 400, 500],
          [150, 250, 350, 450, 550]
        ]
      }]
    },
    options: {
      responsive: true
    }
  });
  