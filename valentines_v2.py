import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(
    page_title="💝 A Special Surprise For You",
    page_icon="💝",
    layout="centered"
)

# Custom CSS for pink cutesy theme
st.markdown("""
<style>
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Background gradient */
    .stApp {
        background: linear-gradient(135deg, #ffd1dc 0%, #ffb6c1 50%, #ffc0cb 100%);
    }
    
    /* Custom styling */
    .main {
        padding: 0rem;
    }
</style>
""", unsafe_allow_html=True)

# Full page HTML component
html_code = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@300;400;600;700&display=swap');
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        html, body {
            overflow: hidden;
            height: 100vh;
            width: 100vw;
        }
        
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #ffd1dc 0%, #ffb6c1 50%, #ffc0cb 100%);
        }
        
        /* Hide all scrollbars */
        ::-webkit-scrollbar {
            display: none;
        }
        
        * {
            -ms-overflow-style: none;
            scrollbar-width: none;
        }
        
        /* Floating hearts background */
        .hearts-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
            overflow: hidden;
        }
        
        .heart-float {
            position: absolute;
            font-size: 20px;
            animation: floatHeart 8s infinite;
            opacity: 0.6;
        }
        
        @keyframes floatHeart {
            0%, 100% { transform: translateY(0) rotate(0deg); }
            50% { transform: translateY(-30px) rotate(15deg); }
        }
        
        /* Main container */
        .container {
            position: relative;
            z-index: 10;
            height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 15px;
            overflow: hidden;
        }
        
        /* Stage 1: Bouquet Builder */
        #bouquetStage {
            text-align: center;
            width: 100%;
            max-width: 800px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        
        .greeting {
            font-family: 'Pacifico', cursive;
            font-size: 2em;
            color: #ff69b4;
            margin: 10px 0;
            text-shadow: 2px 2px 4px rgba(255, 105, 180, 0.2);
            animation: greetingFade 1s ease-in;
        }
        
        @keyframes greetingFade {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .title {
            font-family: 'Pacifico', cursive;
            font-size: 2.2em;
            color: #ff1493;
            margin: 5px 0;
            text-shadow: 2px 2px 4px rgba(255, 105, 180, 0.3);
        }
        
        .subtitle {
            font-size: 1em;
            color: #c71585;
            margin-bottom: 15px;
            font-weight: 300;
        }
        
        /* Flower palette */
        .flower-palette {
            background: rgba(255, 255, 255, 0.7);
            border-radius: 15px;
            padding: 15px;
            margin: 10px 0;
            box-shadow: 0 8px 20px rgba(255, 105, 180, 0.2);
            width: 100%;
            max-width: 500px;
        }
        
        .palette-title {
            font-size: 1.1em;
            color: #ff1493;
            margin-bottom: 10px;
            font-weight: 600;
        }
        
        .flowers-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-bottom: 10px;
        }
        
        .flower-item {
            background: white;
            border-radius: 12px;
            padding: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            border: 2px solid transparent;
            position: relative;
        }
        
        .flower-item:hover {
            transform: translateY(-3px) scale(1.05);
            border-color: #ff69b4;
            box-shadow: 0 6px 15px rgba(255, 105, 180, 0.3);
        }
        
        .flower-icon {
            font-size: 2.2em;
            margin-bottom: 3px;
            display: inline-block;
            animation: flowerBob 2s ease-in-out infinite;
        }
        
        @keyframes flowerBob {
            0%, 100% { transform: translateY(0) rotate(0deg); }
            50% { transform: translateY(-5px) rotate(5deg); }
        }
        
        .flower-name {
            font-size: 0.75em;
            color: #ff1493;
            font-weight: 600;
        }
        
        .flower-meaning {
            position: absolute;
            bottom: 100%;
            left: 50%;
            transform: translateX(-50%);
            background: #ff1493;
            color: white;
            padding: 8px 12px;
            border-radius: 8px;
            font-size: 0.75em;
            white-space: nowrap;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s;
            margin-bottom: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
            z-index: 100;
        }
        
        .flower-meaning::after {
            content: '';
            position: absolute;
            top: 100%;
            left: 50%;
            transform: translateX(-50%);
            border: 6px solid transparent;
            border-top-color: #ff1493;
        }
        
        .flower-item:hover .flower-meaning {
            opacity: 1;
        }
        
        /* Your bouquet */
        .your-bouquet {
            background: rgba(255, 255, 255, 0.85);
            border-radius: 15px;
            padding: 15px;
            margin: 10px 0;
            min-height: 80px;
            width: 100%;
            max-width: 500px;
            border: 2px dashed #ffb6c1;
        }
        
        .bouquet-title {
            font-size: 1.1em;
            color: #ff1493;
            margin-bottom: 10px;
            font-weight: 600;
        }
        
        .bouquet-flowers {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            justify-content: center;
            min-height: 50px;
            align-items: center;
        }
        
        .bouquet-flower {
            font-size: 2em;
            animation: popIn 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            position: relative;
            cursor: pointer;
            transition: transform 0.2s;
        }
        
        .bouquet-flower:hover {
            transform: scale(1.2) rotate(10deg);
        }
        
        @keyframes popIn {
            0% { transform: scale(0) rotate(-180deg); opacity: 0; }
            100% { transform: scale(1) rotate(0deg); opacity: 1; }
        }
        
        .bouquet-empty {
            color: #ffb6c1;
            font-size: 0.9em;
            font-style: italic;
        }
        
        .wrap-button {
            background: linear-gradient(45deg, #ff1493, #ff69b4);
            color: white;
            border: none;
            padding: 15px 40px;
            font-size: 1.1em;
            border-radius: 50px;
            cursor: pointer;
            font-weight: 600;
            box-shadow: 0 6px 15px rgba(255, 20, 147, 0.4);
            transition: all 0.3s ease;
            font-family: 'Poppins', sans-serif;
            margin-top: 10px;
        }
        
        .wrap-button:hover:not(:disabled) {
            transform: translateY(-3px);
            box-shadow: 0 10px 25px rgba(255, 20, 147, 0.6);
        }
        
        .wrap-button:disabled {
            background: linear-gradient(45deg, #ddd, #ccc);
            cursor: not-allowed;
            box-shadow: none;
        }
        
        /* Stage 2: Wrapping Animation */
        #wrappingStage {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: 1000;
        }
        
        .wrapping-container {
            position: relative;
            width: 350px;
            height: 450px;
            margin: 0 auto;
            top: 50%;
            transform: translateY(-50%);
        }
        
        .animated-bouquet {
            position: absolute;
            bottom: 100px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            flex-direction: column;
            align-items: center;
            animation: gatherFlowers 1.5s ease-out forwards;
        }
        
        @keyframes gatherFlowers {
            0% {
                transform: translateX(-50%) scale(0.3);
                opacity: 0;
            }
            100% {
                transform: translateX(-50%) scale(1);
                opacity: 1;
            }
        }
        
        .flower-heads {
            display: flex;
            gap: 5px;
            margin-bottom: -20px;
            z-index: 3;
            position: relative;
        }
        
        .animated-flower {
            font-size: 2.8em;
            animation: bloomFlower 0.8s ease-out backwards;
        }
        
        .animated-flower:nth-child(1) { animation-delay: 0.2s; }
        .animated-flower:nth-child(2) { animation-delay: 0.4s; }
        .animated-flower:nth-child(3) { animation-delay: 0.6s; }
        .animated-flower:nth-child(4) { animation-delay: 0.8s; }
        .animated-flower:nth-child(5) { animation-delay: 1s; }
        
        @keyframes bloomFlower {
            0% {
                transform: scale(0) rotate(-90deg);
                opacity: 0;
            }
            100% {
                transform: scale(1) rotate(0deg);
                opacity: 1;
            }
        }
        
        .stems {
            width: 100px;
            height: 160px;
            background: linear-gradient(to bottom, #90EE90 0%, #228B22 100%);
            border-radius: 0 0 50% 50%;
            position: relative;
            z-index: 2;
            animation: growStems 1s ease-out 0.5s backwards;
        }
        
        @keyframes growStems {
            0% {
                height: 0;
                opacity: 0;
            }
            100% {
                height: 160px;
                opacity: 1;
            }
        }
        
        .wrapping-paper {
            position: absolute;
            bottom: 50px;
            left: 50%;
            transform: translateX(-50%);
            width: 250px;
            height: 280px;
            background: linear-gradient(135deg, #FFB6C1 0%, #FFC0CB 50%, #FFB6C1 100%);
            clip-path: polygon(15% 0%, 85% 0%, 100% 100%, 0% 100%);
            z-index: 1;
            animation: wrapPaper 1.5s ease-out 1.8s backwards;
            box-shadow: inset 0 0 30px rgba(255, 255, 255, 0.5);
        }
        
        @keyframes wrapPaper {
            0% {
                transform: translateX(-50%) scaleY(0);
                opacity: 0;
            }
            100% {
                transform: translateX(-50%) scaleY(1);
                opacity: 1;
            }
        }
        
        .ribbon {
            position: absolute;
            bottom: 180px;
            left: 50%;
            transform: translateX(-50%);
            width: 130px;
            height: 35px;
            background: #FF1493;
            z-index: 4;
            animation: tieRibbon 0.8s ease-out 3.3s backwards;
            border-radius: 5px;
        }
        
        .ribbon::before,
        .ribbon::after {
            content: '';
            position: absolute;
            top: 50%;
            width: 0;
            height: 0;
            border: 18px solid transparent;
        }
        
        .ribbon::before {
            left: -36px;
            border-right-color: #FF1493;
            transform: translateY(-50%);
        }
        
        .ribbon::after {
            right: -36px;
            border-left-color: #FF1493;
            transform: translateY(-50%);
        }
        
        .bow {
            position: absolute;
            top: -22px;
            left: 50%;
            transform: translateX(-50%);
            width: 50px;
            height: 50px;
            background: #FF1493;
            border-radius: 50%;
            animation: bowAppear 0.5s ease-out 3.8s backwards;
        }
        
        .bow::before,
        .bow::after {
            content: '';
            position: absolute;
            background: #FF1493;
            border-radius: 50%;
        }
        
        .bow::before {
            width: 35px;
            height: 45px;
            left: -30px;
            top: 2px;
        }
        
        .bow::after {
            width: 35px;
            height: 45px;
            right: -30px;
            top: 2px;
        }
        
        @keyframes tieRibbon {
            0% {
                transform: translateX(-50%) scaleX(0);
                opacity: 0;
            }
            100% {
                transform: translateX(-50%) scaleX(1);
                opacity: 1;
            }
        }
        
        @keyframes bowAppear {
            0% {
                transform: translateX(-50%) scale(0) rotate(180deg);
                opacity: 0;
            }
            100% {
                transform: translateX(-50%) scale(1) rotate(0deg);
                opacity: 1;
            }
        }
        
        /* Fading message overlay */
        .message-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background: rgba(255, 192, 203, 0.95);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 5;
            opacity: 0;
            pointer-events: none;
        }
        
        .message-overlay.active {
            animation: messageSequence 4s ease-in-out forwards;
        }
        
        @keyframes messageSequence {
            0% {
                opacity: 0;
            }
            15% {
                opacity: 1;
            }
            85% {
                opacity: 1;
            }
            100% {
                opacity: 0;
            }
        }
        
        .overlay-text {
            font-family: 'Pacifico', cursive;
            font-size: 3em;
            color: white;
            text-align: center;
            text-shadow: 3px 3px 6px rgba(255, 20, 147, 0.5);
            animation: textZoom 4s ease-in-out;
        }
        
        @keyframes textZoom {
            0% {
                transform: scale(0.5);
                opacity: 0;
            }
            15% {
                transform: scale(1);
                opacity: 1;
            }
            85% {
                transform: scale(1);
                opacity: 1;
            }
            100% {
                transform: scale(1.2);
                opacity: 0;
            }
        }
        
        /* Stage 3: Question */
        #questionStage {
            display: none;
            text-align: center;
            animation: fadeInQuestion 1s ease-in;
        }
        
        @keyframes fadeInQuestion {
            from {
                opacity: 0;
                transform: scale(0.8);
            }
            to {
                opacity: 1;
                transform: scale(1);
            }
        }
        
        .reveal-message {
            font-family: 'Pacifico', cursive;
            font-size: 1.8em;
            color: #ff1493;
            margin: 20px 0;
        }
        
        .big-question {
            font-family: 'Pacifico', cursive;
            font-size: 3em;
            color: #ff1493;
            margin: 20px 0;
            text-shadow: 3px 3px 6px rgba(255, 105, 180, 0.4);
            animation: questionPulse 2s infinite;
        }
        
        @keyframes questionPulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        .buttons-container {
            position: relative;
            min-height: 250px;
            margin-top: 30px;
        }
        
        .btn {
            font-family: 'Poppins', sans-serif;
            font-size: 1.5em;
            padding: 20px 60px;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            font-weight: 600;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease;
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
        }
        
        #yesBtn {
            background: linear-gradient(45deg, #ff1493, #ff69b4);
            color: white;
            top: 30px;
            animation: yesBounce 2s infinite;
        }
        
        #yesBtn:hover {
            transform: translateX(-50%) scale(1.12);
            box-shadow: 0 15px 35px rgba(255, 20, 147, 0.5);
        }
        
        @keyframes yesBounce {
            0%, 100% { transform: translateX(-50%) translateY(0); }
            50% { transform: translateX(-50%) translateY(-10px); }
        }
        
        #noBtn {
            background: linear-gradient(45deg, #ffc0cb, #ffb6c1);
            color: #ff1493;
            top: 130px;
        }
        
        /* Stage 4: Final Message */
        #finalStage {
            display: none;
            padding: 20px;
            max-height: 100vh;
            overflow-y: auto;
            animation: fadeIn 1s ease;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        .celebration {
            text-align: center;
            font-family: 'Pacifico', cursive;
            font-size: 3em;
            color: #ff1493;
            margin: 20px 0;
            animation: celebrate 1s ease;
        }
        
        @keyframes celebrate {
            0% { transform: scale(0); opacity: 0; }
            50% { transform: scale(1.3); }
            100% { transform: scale(1); opacity: 1; }
        }
        
        .love-letter {
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(255, 192, 203, 0.4));
            border-radius: 25px;
            padding: 40px 30px;
            box-shadow: 0 15px 50px rgba(255, 105, 180, 0.4);
            margin: 20px auto;
            max-width: 650px;
            border: 3px solid #ffb6c1;
        }
        
        .message-title {
            font-family: 'Pacifico', cursive;
            font-size: 2em;
            color: #ff1493;
            text-align: center;
            margin-bottom: 20px;
        }
        
        .message-text {
            font-size: 1.1em;
            color: #c71585;
            line-height: 1.8;
            text-align: center;
            margin-bottom: 15px;
        }
        
        .highlight {
            color: #ff1493;
            font-weight: 600;
        }
        
        .signature {
            font-family: 'Pacifico', cursive;
            font-size: 1.8em;
            color: #ff69b4;
            text-align: right;
            margin-top: 25px;
        }
        
        /* Firework effects */
        .firework {
            position: fixed;
            width: 5px;
            height: 5px;
            border-radius: 50%;
            pointer-events: none;
            z-index: 9999;
        }
        
        @keyframes explode {
            0% {
                transform: translate(0, 0);
                opacity: 1;
            }
            100% {
                transform: translate(var(--tx), var(--ty));
                opacity: 0;
            }
        }
        
        /* Falling hearts */
        .hearts-rain {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 9998;
        }
        
        .falling-heart {
            position: absolute;
            font-size: 25px;
            animation: fall linear infinite;
        }
        
        @keyframes fall {
            to {
                transform: translateY(100vh) rotate(360deg);
            }
        }
        
        /* Mobile responsive */
        @media (max-width: 768px) {
            .greeting { font-size: 1.5em; }
            .title { font-size: 1.8em; }
            .big-question { font-size: 2em; }
            .btn { font-size: 1.2em; padding: 15px 45px; }
            .flower-icon { font-size: 2em; }
            .wrapping-container { width: 280px; height: 380px; }
            .overlay-text { font-size: 2em; }
        }
    </style>
</head>
<body>
    <div class="hearts-bg" id="heartsBg"></div>
    <div class="container">
        <!-- Stage 1: Bouquet Builder -->
        <div id="bouquetStage">
            <div class="greeting">Hi, Chishu! 💕</div>
            <div class="title">🌸 Create Your Bouquet 🌸</div>
            <div class="subtitle">Pick flowers that speak to your heart... each one has a special meaning 💕</div>
            
            <div class="flower-palette">
                <div class="palette-title">Choose Your Flowers</div>
                <div class="flowers-grid">
                    <div class="flower-item" onclick="addFlower('🌹', 'Rose')">
                        <div class="flower-meaning">Love & Passion</div>
                        <div class="flower-icon">🌹</div>
                        <div class="flower-name">Rose</div>
                    </div>
                    <div class="flower-item" onclick="addFlower('🌷', 'Tulip')">
                        <div class="flower-meaning">Perfect Love</div>
                        <div class="flower-icon">🌷</div>
                        <div class="flower-name">Tulip</div>
                    </div>
                    <div class="flower-item" onclick="addFlower('🌺', 'Hibiscus')">
                        <div class="flower-meaning">Delicate Beauty</div>
                        <div class="flower-icon">🌺</div>
                        <div class="flower-name">Hibiscus</div>
                    </div>
                    <div class="flower-item" onclick="addFlower('🌻', 'Sunflower')">
                        <div class="flower-meaning">Adoration & Joy</div>
                        <div class="flower-icon">🌻</div>
                        <div class="flower-name">Sunflower</div>
                    </div>
                    <div class="flower-item" onclick="addFlower('🌼', 'Daisy')">
                        <div class="flower-meaning">Innocence & Purity</div>
                        <div class="flower-icon">🌼</div>
                        <div class="flower-name">Daisy</div>
                    </div>
                    <div class="flower-item" onclick="addFlower('💐', 'Bouquet')">
                        <div class="flower-meaning">Gratitude</div>
                        <div class="flower-icon">💐</div>
                        <div class="flower-name">Mixed</div>
                    </div>
                    <div class="flower-item" onclick="addFlower('🏵️', 'Rosette')">
                        <div class="flower-meaning">Award Winning</div>
                        <div class="flower-icon">🏵️</div>
                        <div class="flower-name">Rosette</div>
                    </div>
                    <div class="flower-item" onclick="addFlower('🌸', 'Cherry')">
                        <div class="flower-meaning">Fleeting Beauty</div>
                        <div class="flower-icon">🌸</div>
                        <div class="flower-name">Cherry</div>
                    </div>
                    <div class="flower-item" onclick="addFlower('💮', 'White Flower')">
                        <div class="flower-meaning">Purity & Truth</div>
                        <div class="flower-icon">💮</div>
                        <div class="flower-name">White</div>
                    </div>
                </div>
            </div>
            
            <div class="your-bouquet">
                <div class="bouquet-title">✨ Your Bouquet ✨</div>
                <div class="bouquet-flowers" id="bouquetFlowers">
                    <div class="bouquet-empty">Click flowers above to add them to your bouquet</div>
                </div>
            </div>
            
            <button class="wrap-button" id="wrapBtn" onclick="wrapBouquet()" disabled>
                🎀 Wrap My Bouquet 🎀
            </button>
        </div>
        
        <!-- Stage 2: Wrapping Animation -->
        <div id="wrappingStage">
            <div class="wrapping-container">
                <div class="animated-bouquet">
                    <div class="flower-heads" id="animatedFlowerHeads"></div>
                    <div class="stems"></div>
                </div>
                <div class="wrapping-paper"></div>
                <div class="ribbon">
                    <div class="bow"></div>
                </div>
            </div>
            <div class="message-overlay" id="messageOverlay">
                <div class="overlay-text">
                    You picked all my favorites! 💕<br>
                    Here's something special...
                </div>
            </div>
        </div>
        
        <!-- Stage 3: Question -->
        <div id="questionStage">
            <div class="big-question">💝 Will You Be My Valentine? 💝</div>
            
            <div class="buttons-container">
                <button id="yesBtn" class="btn" onclick="sayYes()">Yes! 💕</button>
                <button id="noBtn" class="btn">No</button>
            </div>
        </div>
        
        <!-- Stage 4: Final Message -->
        <div id="finalStage">
            <div class="hearts-rain" id="heartsRain"></div>
            <div class="celebration">🎉 Yayyy! She Said Yes! 🎉</div>

            <div class="love-letter">
                <div class="message-title">💝 To My Beautiful Chishu 💝</div>

                <div class="message-text">
                    From the moment we met working on that Master's project, my world became <span class="highlight">brighter</span>, 
                    my days became <span class="highlight">sweeter</span>, and my heart became <span class="highlight">fuller</span>. I still can't believe it all started with calls and late-night coding sessions!
                </div>

                <div class="message-text">
                    You make me laugh when I want to cry, you lift me up when I'm down, 
                    and you make every ordinary moment feel <span class="highlight">extraordinary</span> even when we're just watching shows or sitting together in silence.
                </div>

                <div class="message-text">
                    Being with you feels like coming home. Your smile is my favorite sight, 
                    your laugh is my favorite sound, and your happiness is my favorite mission. Seriously, that laugh… it just melts me.
                </div>

                <div class="message-text">
                    This Valentine's Day, and every day, I want you to know that 
                    <span class="highlight">you are cherished</span>, <span class="highlight">you are adored</span>, 
                    and <span class="highlight">you are loved beyond measure</span>. It's been amazing building this life with you, especially since I proposed in April of 2022 it's hard to believe it's only going to be 4 years until 2026!
                </div>

                <div class="message-text">
                    Thank you for being mine, for saying yes, and for being the most amazing person I know. We've had our ups and downs, and we're still stronger because of it our connection is truly something special. I adore your mischievous side, especially when it's just for me! 💕 
                </div>

                <div class="message-text" style="font-size: 1.3em; margin-top: 20px;">
                    Happy Valentine's Day, my love! 💖  I'm so lucky to have you, Sejal.
                </div>

                <div class="signature">Forever Yours, Amandeep 💕</div>
            </div>
        </div>
    </div>
    
    <script>
        let bouquetFlowers = [];
        
        // Create floating hearts background
        function createBackgroundHearts() {
            const bg = document.getElementById('heartsBg');
            const hearts = ['💕', '💖', '💗', '💓', '💝', '💘'];
            
            for (let i = 0; i < 12; i++) {
                const heart = document.createElement('div');
                heart.className = 'heart-float';
                heart.textContent = hearts[Math.floor(Math.random() * hearts.length)];
                heart.style.left = Math.random() * 100 + '%';
                heart.style.top = Math.random() * 100 + '%';
                heart.style.animationDelay = Math.random() * 4 + 's';
                bg.appendChild(heart);
            }
        }
        
        createBackgroundHearts();
        
        // Add flower to bouquet
        function addFlower(emoji, name) {
            bouquetFlowers.push(emoji);
            updateBouquet();
            
            // Enable wrap button if at least 3 flowers
            document.getElementById('wrapBtn').disabled = bouquetFlowers.length < 3;
        }
        
        // Update bouquet display
        function updateBouquet() {
            const container = document.getElementById('bouquetFlowers');
            if (bouquetFlowers.length === 0) {
                container.innerHTML = '<div class="bouquet-empty">Click flowers above to add them to your bouquet</div>';
            } else {
                container.innerHTML = bouquetFlowers.map((flower, idx) => 
                    `<div class="bouquet-flower" onclick="removeFlower(${idx})" title="Click to remove">${flower}</div>`
                ).join('');
            }
        }
        
        // Remove flower from bouquet
        function removeFlower(index) {
            bouquetFlowers.splice(index, 1);
            updateBouquet();
            document.getElementById('wrapBtn').disabled = bouquetFlowers.length < 3;
        }
        
        // Wrap bouquet and proceed to next stage
        function wrapBouquet() {
            // Hide bouquet stage
            document.getElementById('bouquetStage').style.display = 'none';
            
            // Show wrapping animation
            const wrappingStage = document.getElementById('wrappingStage');
            wrappingStage.style.display = 'block';
            
            // Display animated flowers
            const flowerHeads = document.getElementById('animatedFlowerHeads');
            flowerHeads.innerHTML = bouquetFlowers.slice(0, 5).map((flower, idx) => 
                `<div class="animated-flower">${flower}</div>`
            ).join('');
            
            // Show fading message after wrapping completes (4.5 seconds)
            setTimeout(() => {
                document.getElementById('messageOverlay').classList.add('active');
            }, 4500);
            
            // After message fades (4 more seconds), show question
            setTimeout(() => {
                wrappingStage.style.display = 'none';
                document.getElementById('questionStage').style.display = 'block';
                setupNoButton();
            }, 8500);
        }
        
        // Setup "No" button to run away
        function setupNoButton() {
            const noBtn = document.getElementById('noBtn');
            
            function runAway() {
                const maxX = window.innerWidth - noBtn.offsetWidth - 40;
                const maxY = window.innerHeight - noBtn.offsetHeight - 100;
                
                const randomX = Math.random() * Math.max(maxX, 100);
                const randomY = Math.random() * Math.max(maxY - 100, 100) + 50;
                
                noBtn.style.position = 'fixed';
                noBtn.style.left = randomX + 'px';
                noBtn.style.top = randomY + 'px';
                noBtn.style.transform = 'none';
            }
            
            noBtn.addEventListener('mouseenter', runAway);
            noBtn.addEventListener('touchstart', (e) => {
                e.preventDefault();
                runAway();
            });
        }
        
        // Create firework
        function createFirework(x, y) {
            const colors = ['#ff1493', '#ff69b4', '#ffc0cb', '#ff6b9d', '#c71585'];
            const particles = 35;
            
            for (let i = 0; i < particles; i++) {
                const firework = document.createElement('div');
                firework.className = 'firework';
                firework.style.left = x + 'px';
                firework.style.top = y + 'px';
                firework.style.background = colors[Math.floor(Math.random() * colors.length)];
                
                const angle = (Math.PI * 2 * i) / particles;
                const velocity = 120 + Math.random() * 80;
                const tx = Math.cos(angle) * velocity;
                const ty = Math.sin(angle) * velocity;
                
                firework.style.setProperty('--tx', tx + 'px');
                firework.style.setProperty('--ty', ty + 'px');
                firework.style.animation = 'explode 1.2s ease-out forwards';
                
                document.body.appendChild(firework);
                setTimeout(() => firework.remove(), 1200);
            }
        }
        
        // Say yes - trigger fireworks and show final message
        function sayYes() {
            // Create fireworks burst
            const fireworkCount = 18;
            for (let i = 0; i < fireworkCount; i++) {
                setTimeout(() => {
                    const x = Math.random() * window.innerWidth;
                    const y = Math.random() * window.innerHeight * 0.7;
                    createFirework(x, y);
                }, i * 150);
            }
            
            // After fireworks, show final message
            setTimeout(() => {
                document.getElementById('questionStage').style.display = 'none';
                document.getElementById('finalStage').style.display = 'block';
                startHeartsRain();
            }, 3200);
        }
        
        // Falling hearts rain
        function startHeartsRain() {
            const heartsRain = document.getElementById('heartsRain');
            
            function createFallingHeart() {
                const heart = document.createElement('div');
                heart.className = 'falling-heart';
                heart.textContent = ['💕', '💖', '💗', '💓', '💝', '💘'][Math.floor(Math.random() * 6)];
                heart.style.left = Math.random() * 100 + '%';
                heart.style.animationDuration = (Math.random() * 3 + 3) + 's';
                heart.style.opacity = Math.random() * 0.6 + 0.3;
                heartsRain.appendChild(heart);
                
                setTimeout(() => heart.remove(), 6500);
            }
            
            // Initial burst
            for (let i = 0; i < 12; i++) {
                setTimeout(createFallingHeart, i * 100);
            }
            
            // Continuous rain
            setInterval(createFallingHeart, 300);
        }
    </script>
</body>
</html>
"""

# Display the component
components.html(html_code, height=800, scrolling=False)
