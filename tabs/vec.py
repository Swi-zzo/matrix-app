import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def show():
    st.subheader("Vector Visualization")
    st.write("Enter vectors as comma-separated numbers. Example: 1,2 for 2D, 1,2,3 for 3D.")

    # Input vectors
    vec1_text = st.text_input("Vector 1", "1,2")
    vec2_text = st.text_input("Vector 2 (optional)", "2,1")

    # Parse vectors
    try:
        vec1 = np.array(list(map(float, vec1_text.strip().split(","))))
        vec2 = np.array(list(map(float, vec2_text.strip().split(","))))
    except:
        st.error("❌ Could not parse vectors. Check formatting.")
        return

    # Check dimensions
    if vec1.shape[0] != vec2.shape[0]:
        st.warning("⚠️ Both vectors must have the same dimension for visualization.")
        return

    # Plot
    fig = plt.figure()
    if vec1.shape[0] == 2:
        ax = fig.add_subplot(1,1,1)
        ax.quiver(0,0, vec1[0], vec1[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector 1')
        ax.quiver(0,0, vec2[0], vec2[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector 2')
        ax.quiver(0,0, vec1[0]+vec2[0], vec1[1]+vec2[1], angles='xy', scale_units='xy', scale=1, color='g', label='Sum')
        ax.set_xlim(min(0, vec1[0], vec2[0], vec1[0]+vec2[0])-1, max(0, vec1[0], vec2[0], vec1[0]+vec2[0])+1)
        ax.set_ylim(min(0, vec1[1], vec2[1], vec1[1]+vec2[1])-1, max(0, vec1[1], vec2[1], vec1[1]+vec2[1])+1)
        ax.set_aspect('equal')
        ax.grid(True)
        ax.legend()
    elif vec1.shape[0] == 3:
        ax = fig.add_subplot(111, projection='3d')
        ax.quiver(0,0,0, vec1[0], vec1[1], vec1[2], color='r', label='Vector 1')
        ax.quiver(0,0,0, vec2[0], vec2[1], vec2[2], color='b', label='Vector 2')
        ax.quiver(0,0,0, vec1[0]+vec2[0], vec1[1]+vec2[1], vec1[2]+vec2[2], color='g', label='Sum')
        ax.set_xlim([0, max(vec1[0],vec2[0],vec1[0]+vec2[0])+1])
        ax.set_ylim([0, max(vec1[1],vec2[1],vec1[1]+vec2[1])+1])
        ax.set_zlim([0, max(vec1[2],vec2[2],vec1[2]+vec2[2])+1])
        ax.legend()
    else:
        st.warning("⚠️ Only 2D or 3D vectors are supported.")
        return

    st.pyplot(fig)
