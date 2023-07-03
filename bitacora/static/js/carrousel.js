<!-- Asegúrate de incluir la biblioteca jQuery -->
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

<script>
  $(document).ready(function() {
    // Configurar el intervalo de tiempo (3 segundos en este caso)
    var intervalo = 3000;

    // Función para avanzar al siguiente carrusel
    function avanzarCarrusel() {
      $('.carousel').carousel('next');
    }

    // Iniciar el carrusel automáticamente después de un intervalo de tiempo
    setInterval(avanzarCarrusel, intervalo);
  });
</script>
