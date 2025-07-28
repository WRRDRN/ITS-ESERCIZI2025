import React, { useEffect,useState } from 'react'

const url="https://jsonplaceholder.typicode.com/photos";
const FetchComponent = () => {
    const [photos,setPhotos]=useState([]);

    const getData= async function(){
       const  photo=await fetch(url).then(ris=>ris.json())
       setPhotos(photo)

    }

    useEffect(()=>{
        getData();
    },[])

  return (
    <>
      <h1>Fetch Component</h1>
      <ul className="users">
        {photos.map((el) => {
          const { title, id, thumbnailUrl: img, url } = el;
          return (
            <li key={id} className="shadow">
              <img src={img} alt={title} />
              <div>
                <h5>{id} - {title}</h5>
                <a href={url}> Profile</a>
              </div>
            </li>
          );
        })}
      </ul>
    </>
  )
}

export default FetchComponent