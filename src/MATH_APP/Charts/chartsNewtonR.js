
//static  for now
const datos = [
    391.0,
    218.8852672750978,
    130.90248129301588,
    83.85232034524876,
    55.79865604571236,
    34.872925649637224,
    10.05609847839667,
    -324.01070700967796,
    -133.51977066897746,
    -34.57904946163262,
    30.012174074235887,
    0.4723278137972784,
    155.02960474644837,
    97.11773106805396,
    64.18949530235555,
    41.847515797848544,
    20.27082950848723,
    -35.12602576317225,
    29.46213495974783
  ];

  // Etiquetas (opcional)
  const etiquetas = datos.map((_, index) => `Dato ${index + 1}`);

  // Configuración del gráfico
  const ctx = document.getElementById('myChart').getContext('2d');
  const myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: etiquetas, // Si quieres etiquetas en el eje x
      datasets: [{
        label: 'Datos',
        data: datos,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: false
        }
      }
    }
  });
