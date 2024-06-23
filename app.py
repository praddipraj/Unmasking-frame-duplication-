import streamlit as st 
from detect import detect_duplicates, clear_folders
import time 
import os
from PIL import Image

def main():
    
    st.title('Duplicate Frame Detection')
    clear_folders()
    up_vdo = st.file_uploader('Upload a video file (<10fps)', type=['mp4', 'avi'])
    start = time.time() 
    if up_vdo:
        with open('./input/input.mp4', 'wb') as f:
            f.write(up_vdo.read())
            
        if st.button('Detect'):
            frame_count, dup_count = detect_duplicates('./input/input.mp4')
            end = time.time() 
            elapsed_time = end-start
            st.write('Completed')
            st.write(f'Total Frame Count: {frame_count}')
            st.write(f'Total Duplicate Frames: {dup_count}')
            st.write(f'Elapsed Time: {elapsed_time}')
                    
            
            dup_list = os.listdir('./duplicates/')
            if len(dup_list)>1:
                st.warning('Sample Duplicate Frames')
                comp1 = Image.open('./duplicates/'+dup_list[0])
                comp2 = Image.open('./duplicates/'+dup_list[1])
                st.image([comp1, comp2])
            
            
            
            
            
if __name__=='__main__':
    main()
