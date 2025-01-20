export const fetchItems = async () => {
    const response = await fetch('http://localhost:5000/items');
    return response.json();
  };
  
  export const addItem = async (name, description) => {
    const response = await fetch('http://localhost:5000/items', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, description }),
    });
    return response.json();
  };
  