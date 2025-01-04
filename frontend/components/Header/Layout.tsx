import React from 'react'

const Header = () => {
    const placeHolder="Developer"
  return (
    <header className='flex justify-between items-start mx-10 my-2 '>
        <div className='flex items-center'>
            <img src="/logo.png" alt="" className='max-h-[3.5rem]'/>
            <h1>Logged in as {placeHolder}</h1>
        </div>
        <button>
            Logout
        </button>
    </header>
  )
}

export default Header
