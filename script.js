document.getElementById('uploadButton').addEventListener('click', () => {
        const file = document.getElementById('photoInput').files[0];
        if (file) {
            const formData = new FormData();
            formData.append('photo', file);
            fetch('/upload', {
                method: 'POST',
                body: formData,
            }).then(response => {
                if (response.ok) {
                    alert('uploaded');
                } else {
                    alert('not uploaded');
                }
            });
        } else {
            alert('Pick a photo first!');
        }
    });
