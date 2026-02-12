//import { useState } from 'react'
import './App.css'
import cards from "./cards.jpg";


function App() {

  return (
  <>
  <p className="line-1 anim-typewriter-stop" style={{ animationDelay: "1s" }}>blackjack</p>

  <p className="line-2 anim-typewriter" style={{ animationDelay: "4s" }}>beat the odds.</p>
  <img src={cards} alt="a set of blackjack" className="cards" />
  </>
  )
}

export default App
