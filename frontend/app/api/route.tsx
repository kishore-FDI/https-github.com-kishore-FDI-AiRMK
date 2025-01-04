import { NextResponse } from "next/server";

const BACKEND_URL = 'https://portfoliobackend-ubbd.onrender.com';

export async function POST(req:any) {
  try {
    const { message } = await req.json();

    // const formattedHistory = history.map((msg: { text: any; sender: string; }) => ({
    //   content: msg.text,
    //   role: msg.sender === 'bot' ? 'assistant' : 'user'  
    // }));

    // const filteredHistory = formattedHistory.filter((msg: { content: string; }) => 
    //   msg.content !== 'Hello! How can I assist you?'
    // );
    
    // let Chat = "";
    // filteredHistory.forEach((msg: { role: any; content: any; }, index: number) => {
    //   Chat += `${msg.role}:${msg.content}`;
    //   if (index < filteredHistory.length - 1) {
    //     Chat += ",";
    //   }
    // });
    // console.log(Chat)
    
    const response = await fetch(`${BACKEND_URL}/query`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ 
        question: message,
      })
    });

    if (!response.ok) {
      throw new Error(`Backend responded with status ${response.status}`);
    }

    const data = await response.json();
    console.log(data['answer'])
    return NextResponse.json({
      reply: data["answer"],
    //   chat:message
    });

  } catch (error) {
    console.error("Error:", error);
    return NextResponse.json(
      { error: "Failed to process request. Please try again." },
      { status: 500 }
    );
  }
}