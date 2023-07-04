import streamlit as st
import time
from PIL import Image

st.set_page_config(page_title="CV.Maria Gisela Dora kelen", page_icon=":tada:", layout="wide")

######
# Header
if "file" not in st.session_state:
	st.session_state["file"]="not done"

col1,col2,col3 = st.columns([1,2,1]) 

col1.markdown(" # Maria Gisela Dora Kelen :wave: ")
col1.markdown(" Here is some info about me! ")

image = Image.open("G.png")
st.image(image, width=300)

def change_file_state():
	st.session_state["file"]="done"

uploaded_file = col2.file_uploader("Upload a file", on_change=change_file_state)
browsing_file = col2.file_uploader("Browsing a file", on_change=change_file_state)

if st.session_state["file"] == "done":
	progress_bar = col2.progress(0)

	for perc_completed in range(100):
		time.sleep(0.05)
		progress_bar.progress(perc_completed+1)
	
	col2.success("File uploaded successfully!")

	col3.metric(label="Temperature", value="30 degree celcius", delta="3 degree celcius")

	with st.expander("Click to read more"):
		st.write("Hello, here are more details about my field that you were interested in.")

		if uploaded_file is None:
			st.file_uploader(browsing_file)
		else:
			st.file_uploader(uploaded_file)

st.markdown("## Profil", unsafe_allow_html=True)
st.write("Nama :")
nama = ["Maria Gisela Dora Kelen"]
pilih_nama = st.selectbox("", nama)
if pilih_nama == "Maria Gisela Dora Kelen":
	st.write("")

st.write("TTL :")
TTL = ["Lewotala, 07 Mei"]	
pilih_ttl = st.selectbox("", TTL)
if pilih_ttl == "Lewotala, 07 Mei":
	st.write("")
st.write("Agama :")
agama =["Khatolik"]
pilih_agama = st.selectbox("", agama)
if pilih_agama == "Khatolik":
	st.write("")
st.write("Jenis Kelamin :")
jenis_kelamin = ["Perempuan"]
pilih_jenis_kelamin = st.selectbox("", jenis_kelamin)
if pilih_jenis_kelamin == "Perempuan":
	st.write("")
st.write("Status :")
status = ["Mahasiswi"]
pilih_status = st.selectbox("", status)
if pilih_status == "Mahasiswi":
	st.write("")
st.write("Telepon :")
telepon = ["081219257749"]
pilih_telepon = st.selectbox("", telepon)
if pilih_telepon == "081219257749":
	st.write("")

st.markdown("## Skills", unsafe_allow_html=True)
st.info("""
		- Mampu Mengcoding penyakit
		"""
		)
st.info(""" 
		- Menganalisis Data dengan baik
		"""
		)
st.info("""
		- Interpersonal
		"""
		)
st.info("""
		- Mudah menyesuaikan diri dalam bersosialisasi
		"""	 
		)	

st.markdown("## Education", unsafe_allow_html=True)
st.info("""
		- TKK ST.ELISABETH LEWOTALA
		- SDK LEWOTALA
		- SMPN 2 LARANTUKA
		- SMAN 1 LEWOLEMA
		- UNIVERSITAS NASIONAL KARANGTURI
		"""
		)
st.write(":rainbow:[About UNKARTUR >](https://unkartur.ac.id/)")

st.markdown("## summary", unsafe_allow_html=True)
st.info("""
		- Manajemen Informasi Kesehatan (MIK) sendiri mempelajari sistem informasi kesehatan untuk penyelesaian masalah di bidang kesehatan sehingga terciptanya pelayanan kesehatan yang good clinical governance.
		- Manajemen informasi kesehatan mencakup seluruh aktifitas pengelolaan rekam medis yang dimulai dari pengelolaan dan penataan berkas sampai kepada pengelolaan data hingga menghasilkan sebuah informasi kesehatan sesuai kebutuhan.
		"""
		)
st.header(":mailbox: Get In Touch With Me!")

contact_form = """
<form action="https://formsubmit.co/mgiselladk@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea> 
     <button type="submit">Send</button>
</form> 
"""
st.markdown(contact_form, unsafe_allow_html=True)



st.write("""
	contact personal
	"""
	) 
st.info("""	
	Email : mgiselladk@gmail.com
	"""
	)
st.subheader("""
	Sosial Media
	"""
	)
st.info(":rose:[Instagram >](https://instagram.com/mgisella.dk?igshid=MzNlNGNkZWQ4Mg==)")
st.info(":sunflower:[Twitter >](https://twitter.com/MG_DKS?t=UA38P2G1xS473v8fCAQBdQ&s=09)")
	





