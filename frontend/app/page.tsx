'use client'
import React, { useEffect, useState } from 'react'
import Header from '@/components/Header/Layout'
import Settings from '@/components/Settings/layout'
import ChatScreen from '@/components/Chat/layout'
const page = () => {
  const [sub,setSub]=useState("hi")
  // useEffect(() => {
  //   const test = async () => {
  //     try {
  //       console.log("hi")
  //       const res = await fetch("/api", {
  //         method: "POST",
  //         headers: { "Content-Type": "application/json" },
  //         body: JSON.stringify({
  //           message: "Hi How are You?"
  //         })
  //       })
  //       const { reply } = await res.json(); // Assuming the backend returns 'reply' based on the provided context
  //       setData(reply)
  //       console.log(reply)
  //     } catch (error) {
  //       console.error("Error sending message:", error);
  //     }
  //   }

  //   test()
  // }, [])

  return (
    <main className='flex'>
      <Settings sub={sub} setSub={setSub}/>
      <section className='w-full flex flex-col justify-between'>
        <Header/>
        <ChatScreen sub={sub}/>
      </section>
    </main>
  )
}

export default page
