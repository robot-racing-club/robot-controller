const socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('connect', () => {
  socket.emit('misc', {
    data: 'User Connected'
  });

  const sliders = document.querySelectorAll('input[type="range"]');
  sliders.forEach((slider) => {
    slider.addEventListener('input', (event) => {
      const value = parseInt(event.target.value, 10) - 128;
      const action = slider.getAttribute('name');
      socket.emit('command', {
        action,
        value,
      })
    });
  });
});

socket.on('response', (msg) => {
  console.log(msg);
});