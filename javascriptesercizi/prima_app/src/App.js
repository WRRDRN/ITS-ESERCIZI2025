import './App.css';
import Clock from './Clock';
import Componente1 from './componente1';


function App() {
  let nome="Adriano"
  return (
    <div className="App">
      <Componente1>Adriano</Componente1>
      <h1>Prima App React di {nome} </h1>
      <h2>{
            new Date().toLocaleDateString()+" "+ new Date().toLocaleTimeString()

        }</h2>

      <Clock timezone="9"country="Japan"></Clock>
      <Clock timezone="4"country="Italia"></Clock>
      <Clock timezone="8"country="USA"></Clock>




      
    </div>
  );
}

export default App;
