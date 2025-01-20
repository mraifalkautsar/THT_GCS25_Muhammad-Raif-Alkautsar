import React, { useState } from 'react';

// komponen Child menerima props items dan onAddItem
const Child = ({ items, onAddItem }) => {
  // state untuk menyimpan nilai input name dan description
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');

  // fungsi untuk menangani submit form
  const handleSubmit = (e) => {
    e.preventDefault();
    // panggil fungsi onAddItem dengan parameter name dan description
    onAddItem(name, description);
    // reset nilai input setelah submit
    setName('');
    setDescription('');
  };

  return (
    <div>
      {/* form untuk menambahkan item baru */}
      <form onSubmit={handleSubmit}>
        <input value={name} onChange={e => setName(e.target.value)} placeholder="Name" />
        <input value={description} onChange={e => setDescription(e.target.value)} placeholder="Description" />
        <button type="submit">Add Item</button>
      </form>
      <ul>
        {/* render list items */}
        {items.map(item => (
          <li key={item.id}>{item.name}: {item.description}</li>
        ))}
      </ul>
    </div>
  );
};

export default Child;
