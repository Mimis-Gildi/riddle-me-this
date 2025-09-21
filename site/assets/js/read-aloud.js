function addReadAloudButton() {
    const article = document.querySelector('article, .page__content, main');
    if (!article) return;

    const button = document.createElement('button');
    button.className = 'read-aloud-btn';
    button.innerHTML = '🔊 Read Aloud';
    button.onclick = toggleReadAloud;

    // Insert at top of article
    article.insertAdjacentElement('beforebegin', button);
}

let currentUtterance = null;

function toggleReadAloud() {
    const btn = document.querySelector('.read-aloud-btn');

    if (window.speechSynthesis.paused) {
        window.speechSynthesis.resume();
        btn.innerHTML = '⏸️ Pause';
        return;
    }

    if (window.speechSynthesis.speaking) {
        window.speechSynthesis.pause();
        btn.innerHTML = '▶️ Resume';
        return;
    }


    // Clean the text before reading
    const article = document.querySelector('article, .page__content, main');
    const clone = article.cloneNode(true);

    // Remove elements that shouldn't be read
    clone.querySelectorAll('pre, code, .utterances, script').forEach(el => el.remove());

    const text = clone.innerText;
    currentUtterance = new SpeechSynthesisUtterance(text);

    // Better voice selection
    const voices = window.speechSynthesis.getVoices();
    currentUtterance.voice = voices.find(v => v.lang === 'en-US' && !v.localService) || voices[0];

    currentUtterance.rate = 0.9; // Slightly slower often sounds better

    window.speechSynthesis.speak(currentUtterance);
    btn.innerHTML = '⏸️ Pause';
}

// Auto-add button when page loads
document.addEventListener('DOMContentLoaded', addReadAloudButton);