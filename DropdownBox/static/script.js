// script.js
document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('roundButton');
    const foodList = document.getElementById('foodList');
    const foods = ['うどん', 'カレー', 'アイス', '寿司', 'ラーメン', 'ピザ', 'ハンバーガー', 'パスタ', 'サラダ', '天ぷら', '焼肉', 'そば', 'タコ焼き', '焼きそば', 'ケーキ', 'チョコレート', 'オムライス', 'ステーキ', '唐揚げ', '餃子'];

    foods.forEach((food, index) => {
        const angle = (index / foods.length) * 2 * Math.PI;
        const x = 100 * Math.cos(angle);
        const y = 100 * Math.sin(angle);
        const foodItem = document.createElement('div');
        foodItem.className = 'food-item';
        foodItem.style.transform = `translate(${x}px, ${y}px) rotate(${angle}rad)`;
        foodItem.textContent = food;
        foodList.appendChild(foodItem);
    });

    button.addEventListener('mouseenter', function() {
        foodList.style.display = 'block';
    });

    button.addEventListener('mouseleave', function() {
        foodList.style.display = 'none';
    });
});
