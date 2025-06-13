import React from 'react'

const Componente1 = (props) => {
  console.log(props);
  return (
  
    <>
    <div></div>
    <div>componente1 di {props.children}</div>
    <Anagrafica></Anagrafica>



  </>
  );
};
  const Anagrafica=()=>
      return(<div>Anagrafica<div/>)
}

export default Componente1