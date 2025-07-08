  
    const imageInput = document.getElementById('imageUpload');
    const preview = document.getElementById('preview');
    const resultDiv = document.getElementById('result');
    const sendButton = document.getElementById('sendButton');

    const openCameraButton = document.getElementById('openCamera');
    const cameraStream = document.getElementById('cameraStream');
    const captureButton = document.getElementById('captureButton');
    const stopCameraButton = document.getElementById('stopCameraButton');

    let selectedFile = null;
    let stream = null;

    // 📁 Upload from file
    imageInput.addEventListener('change', (e) => {
      selectedFile = e.target.files[0];
      if (selectedFile) {
        preview.src = URL.createObjectURL(selectedFile);
        preview.style.display = 'block';
      }
    });

    // 📷 Open Camera
    openCameraButton.addEventListener('click', async () => {
      try {
        stream = await navigator.mediaDevices.getUserMedia({ video: true });
        cameraStream.srcObject = stream;
        cameraStream.style.display = 'block';
        captureButton.style.display = 'inline-block';
        stopCameraButton.style.display = 'inline-block';
        resultDiv.innerHTML = "";
      } catch (err) {
        resultDiv.innerHTML = `❌ Camera access denied or unavailable.`;
      }
    });

    // 📸 Capture Frame
    captureButton.addEventListener('click', () => {
      const canvas = document.createElement('canvas');
      canvas.width = cameraStream.videoWidth;
      canvas.height = cameraStream.videoHeight;
      const ctx = canvas.getContext('2d');
      ctx.drawImage(cameraStream, 0, 0);
      canvas.toBlob((blob) => {
        selectedFile = new File([blob], "captured.png", { type: "image/png" });
        preview.src = URL.createObjectURL(selectedFile);
        preview.style.display = 'block';
      });
      resultDiv.innerHTML = "✅ Image captured!";
    });

    // ✖️ Stop Camera
    stopCameraButton.addEventListener('click', () => {
      if (stream) {
        stream.getTracks().forEach(track => track.stop());
      }
      cameraStream.style.display = 'none';
      captureButton.style.display = 'none';
      stopCameraButton.style.display = 'none';
      resultDiv.innerHTML = "✔️ Camera stopped.";
    });

    // 📤 Send to /users/verify_login
    sendButton.addEventListener('click', async () => {
      if (!selectedFile) {
        resultDiv.innerHTML = "❌ Please select or capture an image first.";
        return;
      }

      const formData = new FormData();
      formData.append('image', selectedFile);

      resultDiv.innerHTML = "⏳ Verifying...";

      try {
        const response = await fetch('/users/verify_login', {
          method: 'POST',
          body: formData
        });
        const data = await response.json();
        if (response.ok) {
          resultDiv.innerHTML = `✅ Login successful. Welcome,  <strong>${data.user.name}</strong>`;
        } else {
          resultDiv.innerHTML = `❌ ${data.error}`;
        }
      } catch (error) {
        resultDiv.innerHTML = `❌ Network error.`;
      }
    });
 