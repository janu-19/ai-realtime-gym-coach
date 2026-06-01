import streamlit as st
import os
from services.persistence.exercise_repository import get_or_create_user


def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True

    # 1. Custom Hero Header & Title Section
    st.markdown(
        """
        <div class="lp-hero" style="text-align: center;">
            <div class="lp-logo" style="text-align: center;">⚡ AI COACH</div>
            <h1 class="lp-title" style="text-align: center;">TRAIN SMART.<br><span>PERFECT YOUR FORM.</span></h1>
            <p class="lp-subtitle" style="text-align: center;">
                AI Coach brings a professional trainer directly to your screen. Using real-time computer vision and conversational AI, it provides immediate audio feedback and checks your posture to maximize every rep.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 2. Display the Stunning Futuristic Gym Coach Hero Illustration
    hero_img_path = os.path.join("static", "HERO.jpg")
    if os.path.exists(hero_img_path):
        st.image(hero_img_path, width="stretch")

    st.markdown("<br><br>", unsafe_allow_html=True)

    # 3. Dynamic Exercise Showcase Cards
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 2rem;">
            <h2 style="margin-bottom: 0.5rem; font-size: 2.2rem; font-weight: 800;">EXPLORE THE ARENA</h2>
            <p style="color: #9CA3AF; font-size: 1rem; max-width: 600px; margin: 0 auto;">
                Experience interactive, real-time pose tracking optimized for five primary compounds.
            </p>
        </div>
        
        <div class="lp-grid">
            <div class="lp-card">
                <div class="lp-badge lp-badge-lower">Lower Body</div>
                <div class="lp-card-icon">🏋️‍♂️</div>
                <div class="lp-card-title">Squats</div>
                <div class="lp-card-desc">Perfect your squat depth and spine alignment. Ideal for quad and glute activation.</div>
            </div>
            <div class="lp-card">
                <div class="lp-badge lp-badge-upper">Upper Body</div>
                <div class="lp-card-icon">🤸‍♂️</div>
                <div class="lp-card-title">Push-ups</div>
                <div class="lp-card-desc">Ensure straight body alignment and monitor elbow contraction. Excellent for chest and core.</div>
            </div>
            <div class="lp-card">
                <div class="lp-badge lp-badge-upper">Arms</div>
                <div class="lp-card-icon">💪</div>
                <div class="lp-card-title">Biceps Curls</div>
                <div class="lp-card-desc">Minimize torso swing and elbow drift to keep constant tension on the biceps.</div>
            </div>
            <div class="lp-card">
                <div class="lp-badge lp-badge-upper">Shoulders</div>
                <div class="lp-card-icon">⬆️</div>
                <div class="lp-card-title">Shoulder Press</div>
                <div class="lp-card-desc">Track full arm extension and monitor back arching for optimal overhead strength safety.</div>
            </div>
            <div class="lp-card">
                <div class="lp-badge lp-badge-lower">Legs & Balance</div>
                <div class="lp-card-icon">🏃‍♂️</div>
                <div class="lp-card-title">Lunges</div>
                <div class="lp-card-desc">Monitor front-knee angle and lateral sway offset to master stability and quad isolation.</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # 4. Core Features Showcase Row
    st.markdown(
        """
        <div class="lp-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); margin-bottom: 4rem;">
            <div class="lp-card" style="display: flex; align-items: center; text-align: left; padding: 1.5rem; gap: 1.25rem;">
                <span style="font-size: 2.2rem;">🎙️</span>
                <div>
                    <h4 style="margin: 0 0 0.25rem 0; color: #fff; font-weight: 700;">Real-Time Voice Coaching</h4>
                    <p style="margin: 0; font-size: 0.85rem; color: #9CA3AF;">Proactive, low-latency audio cues from an LLM coach keep your form safe and perfect.</p>
                </div>
            </div>
            <div class="lp-card" style="display: flex; align-items: center; text-align: left; padding: 1.5rem; gap: 1.25rem;">
                <span style="font-size: 2.2rem;">📊</span>
                <div>
                    <h4 style="margin: 0 0 0.25rem 0; color: #fff; font-weight: 700;">Deep Metrics Tracking</h4>
                    <p style="margin: 0; font-size: 0.85rem; color: #9CA3AF;">Precision joint angle tracking continuously displays live analytics on depth, swing, and posture.</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    # 5. Illuminated Login / Access Container
    st.markdown(
        """
        <div style="text-align: center; margin-top: 2.5rem; margin-bottom: 1.5rem;">
            <h2 style="font-weight: 800; font-size: 1.8rem; margin-bottom: 0.25rem;">READY TO TRAIN?</h2>
            <p style="color: #9CA3AF; font-size: 0.95rem;">Enter a unique username to launch your customized AI fitness arena.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # stForm styling turns this into a beautiful glass card
    with st.form("login_form", clear_on_submit=False):
        username = st.text_input(
            "Username",
            placeholder="Enter your name ",
            label_visibility="collapsed",
        )
        submit_button = st.form_submit_button("Enter the Arena ⚡")

    if submit_button:
        if not username:
            st.error("Name cannot be empty.")
            return False

        user = get_or_create_user(username)

        st.session_state["user_id"] = user["id"]
        st.session_state["username"] = user["username"]

        st.rerun()

    return False