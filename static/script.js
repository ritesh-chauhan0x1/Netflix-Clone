document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/movies')
        .then(res => res.json())
        .then(movies => {
            const moviesSection = document.getElementById('movies');
            movies.forEach(movie => {
                const movieDiv = document.createElement('div');
                movieDiv.className = 'movie';
                movieDiv.innerHTML = `
                    <img src="${movie.image}" alt="${movie.title}">
                    <div class="movie-title">${movie.title}</div>
                    <div class="movie-desc">${movie.desc}</div>
                `;
                moviesSection.appendChild(movieDiv);
            });
        });
});
