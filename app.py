import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def fourier_series_square_wave(x, n):
    sum = np.zeros_like(x)
    for k in range(1, 2*n, 2):
        sum += np.sin(k * x) / k
    return 4 / np.pi * sum


def fourier_series_sawtooth_wave(x, n):
    sum = np.zeros_like(x)
    for k in range(1, n+1):
        sum += ((-1)**(k+1) * np.sin(k * x)) / k
    return 2 / np.pi * sum

def custom_sawtooth(t, width=1):
    # Ensure width is within [0, 1]
    width = np.clip(width, 0, 1)
    
    # Create the sawtooth waveform
    y = 2 * (t / (2 * np.pi * width) - np.floor(0.5 + t / (2 * np.pi * width)))
    
    # Adjusting for width
    y = np.where(t % (2 * np.pi) < 2 * np.pi * width, y / 2 + 0.5, y / 2 - 0.5)

    return y


# Actual waveforms
def actual_square_wave(x):
    return np.sign(np.sin(x))

def actual_triangular_wave(x):
    return 2 * np.abs(2 * ((x - np.pi/2) / (2*np.pi) - np.floor((x - np.pi/2) / (2*np.pi) + 1/2))) - 1

st.markdown(
        f"""
<style>
    .appview-container .main .block-container{{
        max-width: 1550px;
        padding-top: 50px;
        padding-right: 200px;
        padding-left: 10px;
        padding-bottom: 10px;
    }}
    iframe{{
     width: 800px;
     margin:auto;
     display:block;
    }}
</style>
""",
        unsafe_allow_html=True,
    )

# Streamlit app title
st.sidebar.title('Fourier Series Approximation of Waveforms')

# Sidebar slider for the number of terms
n = st.sidebar.slider('Number of Terms (n)', 1, 50, 5)

col1, col2 = st.columns(2)

with col1:
    def write_terms(n):
        terms = []
        for k in range(1, 2*n, 2):
            term = r"\frac{{\sin({}x)}}{{{}}}".format(k, k)
            terms.append(term)
        series_latex = r"f(x) = \frac{4}{\pi} \left(" + " + ".join(terms) + r"\right)"
        st.latex(series_latex)

    write_terms(n)   

    st.latex(r"f(x) = \frac{4}{\pi} \sum_{k=1,3,5,\ldots}^{\infty} \frac{\sin(kx)}{k}")

# Create a set of x values from -π to π
x = np.linspace(-np.pi, np.pi, 1000)

# Compute the Fourier series approximation based on selected waveform
y = fourier_series_square_wave(x, n)
actual_y = actual_square_wave(x)

with col2:    
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    # Plotting
    fig, ax = plt.subplots()

    # Plot the Fourier series approximation
    ax.plot(x, y, label='Fourier Approximation')

    # Plot the actual waveform
    ax.plot(x, actual_y, color='green', label='Actual Waveform')

    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_title(f'Fourier Series Approximation with n = {n} for Square Wave')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True)
    ax.legend()

    # Show plot in Streamlit
    st.pyplot(fig)
