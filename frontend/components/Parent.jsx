import React, { useState, useEffect } from 'react';
import Child from './Child';
import { fetchItems, addItem } from '../src/api/items.js';

const Parent = () => {
  const [items, setItems] = useState([]);

  // ambil item
  useEffect(() => {
    fetchItems().then(setItems);
  }, []);

  // penanganan tambah item
  const handleAddItem = (name, description) => {
    addItem(name, description).then(newItem => {
      setItems(prev => [...prev, newItem]);
    });
  };

  return (
    <div>
      <Child items={items} onAddItem={handleAddItem} />
    </div>
  );
};

export default Parent;
