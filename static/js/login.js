 document.addEventListener('DOMContentLoaded', function() {
            // Button hover effects
            const buttons = document.querySelectorAll('.btn-cyclo, .google-btn');
            
            buttons.forEach(button => {
                button.addEventListener('mouseenter', function() {
                    this.style.transition = 'all 0.3s ease';
                });
            });
        });