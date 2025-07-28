import React, { useState } from 'react'
import axios from 'axios'
const url="https://jsonplaceholder.typicode.com/users"
const Rendercondizionale = () => {


    const[isLoading,setIsLoading]=useState(True)
    const[isError,setIsError]=useState(true)
    const[users,setUsers]=useState([])

    const getData=async()=> {
        setIsError(false);
        setIsLoading(true);
        try{


        }catch(err){
            console.log(err)
                setIsError(True)
        }
    }

if(isLoading){
    return<h2>Loading</h2>
}
if(isError){
    return(<h2>Attenzione,error</h2>)
}
  return (
    <div>rendercondizionale</div>
  )
}

const Loading=()=>{
    return(<h2>Loading</h2>)
}

export default Rendercondizionale