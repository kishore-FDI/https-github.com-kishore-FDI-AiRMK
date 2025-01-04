import React, { useEffect, useState } from 'react';

const ChatScreen = ({ sub }: { sub: string }) => {
  const [data, setData] = useState('');
  const [input, setInput] = useState(''); 

  const fetchData = async (message: string) => {
    try {
      const response = await fetch("/api", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
      });
      const { reply } = await response.json();
      setData(reply);
      console.log(reply);
    } catch (error) {
      console.error("Error sending message:", error);
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault(); 
    if (input.trim()) {
      fetchData(input); 
      setInput(''); 
    }
  };

  return (
    <section>
      {data && <p>{data}</p>}
      <form onSubmit={handleSubmit} className="mb-6">
        <div className="bg-black flex rounded-xl">
          <input
            type="text"
            value={input} 
            onChange={(e) => setInput(e.target.value)} 
            placeholder={`Query about ${sub}`}
            className="p-2 w-full bg-transparent outline-none text-white"
          />
          <button
            type="submit"
            className="bg-blue-500 text-white px-4 py-2 rounded-xl ml-2"
          >
            Send
          </button>
        </div>
      </form>
    </section>
  );
};

export default ChatScreen;
