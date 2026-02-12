//import { useState } from 'react'
import './App.css'
import cards from "./cards.png";


function App() {

  return (
  <>
  <p className="line-1 anim-typewriter-stop" style={{ animationDelay: "1s" }}>BLACKJACK</p>

  <p className="line-2 anim-typewriter" style={{ animationDelay: "3s" }}>beat the odds.</p>
  <img src={cards} alt="a set of blackjack" className="cards" />
  </>
  )
}

export default App
