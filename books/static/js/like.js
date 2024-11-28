function toggleLike(reviewId, csrfToken) {
    fetch(`/reviews/like/${reviewId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken,
            'Content-Type': 'application/json',
        }
    })
    .then(response => response.json())
    .then(data => {
        const likeButton = document.querySelector(`#like-button-${reviewId}`);
        if (data.liked) {
            likeButton.textContent = `いいね (${data.likes_count})`;
            likeButton.classList.remove('btn-outline-primary');
            likeButton.classList.add('btn-primary');
        } else {
            likeButton.textContent = `いいね (${data.likes_count})`;
            likeButton.classList.remove('btn-primary');
            likeButton.classList.add('btn-outline-primary');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
