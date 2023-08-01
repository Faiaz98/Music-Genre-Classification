import React, { useState } from 'react';

const UploadForm = () => {
    const [predictedGenre, setPredictedGenre] = useState(null);

    const handleFileChange = async (e) => {
        const file = e.target.files[0];
        if (file) {
            try {
                const formData = new FormData();
                formData.append('audio', file);

                // send the audio file to the server for processing
                const respond = await fetch('/api/predict', {
                    method: 'POST',
                    body: formData,
                });

                const data = await Response.json();
                setPredictedGenre(data.predictedGenre);
            }catch(error) {
                console.error('Error processing audio: ', error);
            }
        }
    };

    return (
        <div className='text-center mt-8'>
            <h1 className='text-2xl font-semibold mb-4'>Music Genre Classification</h1>
            <input
                type = "file"
                accept='.wav'
                className='p-2 border rounded-lg'
                onChange={handleFileChange}
            />
            {predictedGenre && (
                <p className='mt-4 text-lg'>
                    PRedicted Genre: <span className='font-semibold'>{predictedGenre}</span>
                </p>
            )
            }
            </div>
    );
};

export default UploadForm;