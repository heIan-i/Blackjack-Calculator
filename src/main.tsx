import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
//import PythonRunner from './PythonRunner.tsx'


createRoot(document.getElementById('root')!).render(
  <StrictMode>
    {/*<PythonRunner >*/}
    <App />
  </StrictMode>,
)
