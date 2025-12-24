const yearEl = document.getElementById('year');
if (yearEl) yearEl.textContent = new Date().getFullYear();

const form = document.getElementById('searchForm');
if (form){
  form.addEventListener('submit', (e)=>{
    e.preventDefault();
    const fd = new FormData(form);
    const from = fd.get('from') || '—';
    const to = fd.get('to') || '—';
    const depart = fd.get('depart') || '—';
    // simple feedback
    alert(`Ищем рейсы: ${from} → ${to}\nТуда: ${depart}`);
  });
}

const exploreBtn = document.getElementById('exploreBtn');
if (exploreBtn){
  exploreBtn.addEventListener('click', ()=>{
    const popular = document.getElementById('popular');
    if (popular) popular.scrollIntoView({behavior:'smooth'});
  });
}

/* Support page: FAQ toggle (no support form) */
document.addEventListener('DOMContentLoaded', ()=>{
  // FAQ toggle: attach click handlers to questions
  const faqQuestions = document.querySelectorAll('.faq-question');
  
  faqQuestions.forEach(question => {
    question.addEventListener('click', function() {
      const faqItem = this.parentElement;
      const answer = faqItem.querySelector('.faq-answer');
      const chev = this.querySelector('.chev');
      
      // Переключаем классы для анимации
      answer.classList.toggle('expanded');
      chev.classList.toggle('rotated');
      
      // Изменяем символ в зависимости от состояния
      if (answer.classList.contains('expanded')) {
        chev.textContent = '▾';
      } else {
        chev.textContent = '▸';
      }
    });
 });
});

