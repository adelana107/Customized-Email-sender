 // Initialize WOW.js for scroll animations
        new WOW().init();
        
        // Form submission handler
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.querySelector('.cyclo-form');
            const submitBtn = document.getElementById('submitBtn');
            const spinner = document.getElementById('spinner');
            
            if (form) {
                form.addEventListener('submit', function() {
                    submitBtn.disabled = true;
                    spinner.style.display = 'inline-block';
                    submitBtn.querySelector('i').style.opacity = '0.5';
                });
            }
            
            // Add floating label effect
            const formControls = document.querySelectorAll('.form-control, .form-select');
            
            formControls.forEach(control => {
                // Add focus/blur effects
                control.addEventListener('focus', function() {
                    this.parentElement.querySelector('.input-group-text').style.color = 'var(--cyclo-primary)';
                    this.parentElement.querySelector('.input-group-text').style.backgroundColor = 'rgba(99, 102, 241, 0.05)';
                });
                
                control.addEventListener('blur', function() {
                    this.parentElement.querySelector('.input-group-text').style.color = '';
                    this.parentElement.querySelector('.input-group-text').style.backgroundColor = '';
                });
                
                // Add validation classes
                if (control.classList.contains('is-invalid')) {
                    control.parentElement.querySelector('.input-group-text').style.color = 'var(--cyclo-danger)';
                }
            });
            
            // Animate cards on hover
            const cards = document.querySelectorAll('.cyclo-card, .feature-item');
            cards.forEach(card => {
                card.addEventListener('mouseenter', function() {
                    this.style.transition = 'all 0.3s ease';
                });
            });
            
            // Auto-focus first field with error
            const firstErrorField = document.querySelector('.is-invalid');
            if (firstErrorField) {
                setTimeout(() => {
                    firstErrorField.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    firstErrorField.focus();
                }, 500);
            }
        });