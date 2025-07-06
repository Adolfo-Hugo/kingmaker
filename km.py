import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Pathfinder 2e -  Kingmaker",
    layout="wide",
    page_icon="\U0001F9DD"
)

# Estilo global
st.markdown("""
    <style>
        /* ** Adicione este CSS para remover a barra branca do cabeçalho ** */
        header[data-testid="stHeader"] {
            display: none;
        }
        /* ** Fim do CSS para remover a barra branca ** */

        .titulo-principal {
            font-size: 48px;
            text-align: center;
            color: #f5e8c7;
            margin-top: 30px;
            text-shadow: 2px 2px 4px #000000;
        }
        .descricao {
            font-size: 20px;
            text-align: justify;
            color: #e0d8c3;
            margin: 30px auto;
            max-width: 1000px;
        }
        .subtitulo {
            font-size: 28px;
            color: #f0e6d2;
            margin-top: 40px;
            margin-bottom: 20px;
        }
        .formulario label, .formulario input, .formulario label, .formulario input, .formulario textarea, .formulario select {
            color: #ffffff !important;
        }
        .stApp {
            background-color: #000000;
        }
        section[data-testid="stSidebar"] {
            background-color: #1e1e1e !important;
        }
        .css-1v0mbdj, .css-1cpxqw2, .css-1d391kg, .css-10trblm {
            color: #f5e8c7 !important;
        }
    </style>
""", unsafe_allow_html=True)

# O restante do seu código permanece o mesmo
# Título principal
#st.markdown('<div class="titulo-principal"><u>Trilha de Aventura -  Kingmaker</u></div>', unsafe_allow_html=True)
st.image('km-logo.webp')
# Descrição
st.markdown("""
<div class="descricao">
    <i>Há muito tempo, as Terras Roubadas são o domínio de bandidos e
    monstros, mas isso está para mudar! Seu grupo recebeu uma licença
    para explorar essas regiões selvagens, derrotar seus perigos e erguer
    uma nova nação. No entanto, nem todos vão recebê-los como novos
    vizinhos, e forças sobrenaturais poderosas têm planos para a região.
    Será que vocês conseguirão derrotar os inimigos do seu reino e se
    tornar uma das maiores nações do mundo?</i>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div class="descricao">
    Aventure-se em <strong>Kingmaker</strong>: Conquiste e Governe suas Próprias Terras!<br><br>
    Prepare-se para uma jornada épica do level 1 ao 20  onde suas escolhas moldam o destino de um reino! Em <strong>Kingmaker</strong>, você e seus companheiros não serão apenas aventureiros buscando tesouros, mas sim os pioneiros de uma nova fronteira.<br><br>
    Nesta campanha clássica de RPG, vocês serão encarregados de explorar as traiçoeiras <em>Stolen Lands</em>, desvendando seus segredos, enfrentando feras selvagens e lidando com facções rivais. Mas a aventura não para por aí: à medida que avançam, terão a oportunidade e a responsabilidade de fundar e governar seu próprio reino.
</div>
""", unsafe_allow_html=True)
              
# Vídeo centralizado com autoplay e mudo
VIDEO_URL = "https://www.youtube.com/embed/jR-HjRQPJqI?autoplay=1&mute=1" # Este URL parece incorreto, pode dar erro no vídeo. Verifique se é um link válido do YouTube.
st.markdown(f"""
    <div style="display: flex; justify-content: center;">
        <iframe width="500" height="300" src="{VIDEO_URL}" frameborder="0" 
        allow="autoplay; encrypted-media" allowfullscreen></iframe>
    </div>
""", unsafe_allow_html=True)
# Galeria
st.markdown('<div class="subtitulo">Galeria de Aventuras</div>', unsafe_allow_html=True)
image_urls = [
    "https://i.imgur.com/CCX7oDZ.png",
    "https://i.imgur.com/4rFiTt8.png",
    "https://i.imgur.com/3BbGEu5.png",
    "https://i.imgur.com/2Rx5Vm0.png",
]
if "img_idx" not in st.session_state:
    st.session_state.img_idx = 0
cols = st.columns(len(image_urls))
for idx, col in enumerate(cols):
    with col:
        st.markdown(
            f"""
            <div style="text-align:center;">
                <img src="{image_urls[idx]}" style="height:200px; object-fit:cover; border-radius:8px; border:2px solid #555;">
            </div>
            """,
            unsafe_allow_html=True
        )


# Música de fundo na sidebar
st.sidebar.markdown('<div class="subtitulo">Playlist</div>', unsafe_allow_html=True)
# Removi as importações duplicadas de streamlit e components aqui
AUDIO_URL = [
    "https://audio.jukehost.co.uk/fGl4TvZX4bMpZ4q6sa7BIoqyC35VpS9Q",
    "https://audio.jukehost.co.uk/mn8DcpFMNxKjnY9UWFGrfmT8C0pGN79p",
    "https://audio.jukehost.co.uk/ASy6r08Uc6e920BX2CwMmafPflL2tL7y",
    "https://audio.jukehost.co.uk/b9qjplQBnbPvKdiB0UCjIJyGb4fJgXa1",
    "https://audio.jukehost.co.uk/tm5PtMzKGBMEV3ufCRkqM4uPkJjltHfe",
    "https://audio.jukehost.co.uk/omN3zBDhO1FNsGd24C2E2G4JkvpiFmy3",
    "https://audio.jukehost.co.uk/CXBAGVxC5LpwKUXFEBctmSj2HhsIrgBk",
    "https://audio.jukehost.co.uk/bTdZQyhUcTgRrmQra62OIcg2ZsCDkjjG",
    "https://audio.jukehost.co.uk/6GfAKcKdHpWJr12KR9kJyv2SNI5gumkz",
    "https://audio.jukehost.co.uk/6e1Xu9obL0tOSKxARyBfJgyWqVVGpw5W"
]

track_names = [f"Trilha {i+1}" for i in range(len(AUDIO_URL))]

playlist_js = """
<script>
let tracks = [%s];
let names = [%s];
let currentTrack = 0;

function playNext(audio, display) {
    currentTrack = (currentTrack + 1) %% tracks.length;
    audio.src = tracks[currentTrack];
    display.innerText = names[currentTrack];
    audio.play();
}
window.onload = function() {
    let audio = document.getElementById("playlistAudio");
    let display = document.getElementById("trackName");
    audio.src = tracks[0];
    display.innerText = names[0];
    audio.play();
    audio.onended = function() {
        playNext(audio, display);
    }
}
</script>
""" % (
    ", ".join([f'"{url}"' for url in AUDIO_URL]),
    ", ".join([f'"{name}"' for name in track_names])
)

# Renderizando dentro do sidebar:
with st.sidebar:
    components.html(f"""
        <div style="color:#f5e8c7; font-size:16px; margin-bottom:6px;">
            Tocando agora: <span id="trackName">Carregando...</span>
        </div>
        <audio id="playlistAudio" controls autoplay style="width:230px; height:25px;"></audio>
        {playlist_js}
    """, height=100)


st.sidebar.markdown("""<p style='color:#f0e6d2; font-size:18px; margin-top:40px;'>
                    <strong>MJ: Hugo Silva</strong><br> 
                    </div> 
                    """, unsafe_allow_html=True)

# Link extra do formulário
st.sidebar.markdown("""
<p style='color:#f0e6d2; font-size:18px; margin-top:40px;'>
📋 Formulário de Recrutamento: 
<a href='https://forms.gle/Rfdw51B6349YyvsMA' target='_blank' style='color:#ffd700; text-decoration:none; font-weight:bold;'>clique aqui</a>
</p>
""", unsafe_allow_html=True)
st.sidebar.markdown("""
<p style='color:#f0e6d2; font-size:18px; margin-top:40px;'>
<strong>🌐 Servidor:</strong><br>
<a href='https://discord.gg/y3twcQ6XgA' target='_blank' style='color:#ffd700; text-decoration:none; font-weight:bold;'> Discord</a>
</p>
""", unsafe_allow_html=True)

st.sidebar.markdown("""
<div style="text-align: left; margin-top: 20px; color:#f0e6d2;font-size:18px; margin-top:40px;">
    <strong>📅 Horário:</strong><br>
    Domingo: 20h às 23h <br>
</div>
""", unsafe_allow_html=True)
st.sidebar.markdown("""
<div style="text-align: left; margin-top: 20px; color:#f0e6d2;font-size:18px; margin-top:40px;">
    <strong>💰 Valor: R$20,00/sessão</strong><br>
</div>
""", unsafe_allow_html=True)




st.sidebar.markdown("""
<div style="text-align: left; margin-top: 20px; color:#f0e6d2;font-size:18px; margin-top:40px;">
    <strong>📋 Ferramentas e materiais:</strong><br>
    Foundry VTT<br>
    Discord<br>
    Pathbuilder<br>
    FLC<br>
    Guia do Jogador da campanha<br>
</div>
""", unsafe_allow_html=True)
