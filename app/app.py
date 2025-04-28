import streamlit as st
import random
import time

friend_name = "ZEVTHEFIRST"
short_message = """
Even though we met through PUBG, what started as just random matches turned into a genuine and unforgettable friendship. 
You've been more than just a gaming buddy — you've become someone I truly respect and value. 
Despite the times when we blocked, removed, or even drifted apart, my respect and feelings for you have never changed. 
You are like a kind of magic — someone who just makes things better without even trying. 
Your presence, even from a distance, has had a deep and lasting impact on me.
It's rare to find someone who sticks in your heart like that, no matter what happens. 
You’ve shown me that real and true respect survives all storms. 
I am honestly so proud of you — proud of how far you've come, proud of the strength you carry inside, 
and proud of the person you are becoming. 
I know the hard times you’re facing right now feel heavy, but believe me, they are not forever. 
Better days are on their way, and you are going to be blessed with everything you have been working so hard 
and dreaming so passionately for. 
Your hard work, your struggles, your silent battles — none of it will go wasted. 
The universe has been watching your efforts, and your time to shine is coming. 
Always remember, no matter what, I’ll be cheering for you, believing in you, and wishing you nothing but the absolute best. 
I’m genuinely thankful for you, and I hope this friendship continues to grow, because having someone like you around 
is truly one of the rarest blessings. 
Stay the amazing person you are! MISSYOU hahahhaa <3
"""

def main():
    st.set_page_config(page_title="Friendship Appreciation App", page_icon="🎁")
    
    st.title("🎉 ZEVVO APPRECIATIONNNNNNN POSTTT 🎉")
    st.write("HEYYYOOO THERE IS SOMETHINGGGGGGG FOR YOUUUUUUUU")

    if st.button("1..2..3..CLICK ON THIS BUTTON WITH A SMILEEE PLSS"):
        st.subheader(f"Dear {friend_name},")
        st.success(short_message)

        st.markdown("---")

        st.balloons()

        st.markdown("---")
        
        st.subheader("🎵 A song that reminds me of you:")
        st.video("https://www.youtube.com/watch?v=y8jRZxCQsuY")  # ← Correctly indented here

if __name__ == "__main__":
    main()
