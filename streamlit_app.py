import streamlit as st
import moviepy.editor as me
import tempfile
import speech_recognition as sr
import os

# Function to convert audio to text using Google Web Speech API
def audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language="ar-AR")  # Specify Arabic language
    return text

# Streamlit application
st.title(":orange[Sign Language] :blue[Processing] 👋")
st.markdown(":gray[Effortlessly extract audio from video files and convert them to high-quality MP3s] :violet[for easy NLP further processing.]")
st.divider()

uploaded_video = st.file_uploader(":blue[Please Upload Your Video]", type=["mp4", "mov", "avi", "mkv"])

# Temporarily save the uploaded video file and extract the audio
if uploaded_video is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video_file:
        temp_video_file.write(uploaded_video.read())  # Write the uploaded video to a temp file
        video_path = temp_video_file.name  # Get the temp video file path

    # Extract Audio Button
    if st.button(":orange[Extract Audio]"):
        get_video = me.VideoFileClip(video_path)
        get_audio = get_video.audio

        # Save the extracted audio file in another temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_audio_file:
            audio_path = temp_audio_file.name
            get_audio.write_audiofile(audio_path)

        # Indicate successful audio extraction
        st.success("Audio extracted successfully!")  

        # Display extracted audio playback
        st.audio(audio_path)

        # Store audio_path in session state to access it later
        st.session_state.audio_path = audio_path

        st.divider()

    # Convert audio to text when the button is clicked
    if st.button(":orange[Convert Audio to Text]"):
        if 'audio_path' in st.session_state:  # Check if audio_path is available
            extracted_text = audio_to_text(st.session_state.audio_path)  # Extract text from audio
            st.subheader("Extracted Text from Audio:")
            st.text_area("Extracted Text", extracted_text, height=300)  # Display extracted text in a text area
        else:
            st.error("Please extract audio first.")
