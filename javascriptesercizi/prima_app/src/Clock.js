import React from 'react'

const Clock = (props) => {
    console.log(props.timezone.country)
    const t=Date.now()+3600*props.timezone*1000;
    const date=new Date (t);
  return (
    <div>
    
       In {props.country} sono le {date.toLocaleDateString()+" "+ date.toLocaleTimeString()}
        
   

    </div>
  )
}

export default Clock     
