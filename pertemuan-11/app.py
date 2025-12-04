import streamlit as st
st.title("Form Data Diri")
st.write("Silakan isi data diri Anda di bawah ini:")
st.write("made by Agung")

with st.form("form_data_diri"):
    nama = st.text_input("Nama Lengkap")
    alamat = st.text_input("Alamat")
    usia = st.number_input("Usia")
    submit = st.form_submit_button("Submit")
    if submit:
        st.success(f"Data berhasil disubmit! Nama: {nama}, Alamat: {alamat}, Usia: {usia}")
        st.write(f"Nama Lengkap: {nama}")
        st.write(f"Alamat: {alamat}")
        st.write(f"Usia: {usia}")