 // Create confetti effect
        document.addEventListener('DOMContentLoaded', function() {
            const colors = ['#4361ee', '#3a0ca3', '#f72585', '#4cc9f0'];
            const container = document.querySelector('.success-container');
            
            for (let i = 0; i < 50; i++) {
                setTimeout(() => {
                    const confetti = document.createElement('div');
                    confetti.className = 'confetti';
                    confetti.style.left = Math.random() * 100 + '%';
                    confetti.style.top = -10 + 'px';
                    confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
                    confetti.style.width = Math.random() * 8 + 5 + 'px';
                    confetti.style.height = Math.random() * 8 + 5 + 'px';
                    confetti.style.borderRadius = Math.random() > 0.5 ? '50%' : '0';
                    confetti.style.animation = `confetti-fall ${Math.random() * 3 + 2}s linear forwards`;
                    container.appendChild(confetti);
                    
                    // Remove confetti after animation
                    setTimeout(() => {
                        confetti.remove();
                    }, 5000);
                }, Math.random() * 2000);
            }
        });