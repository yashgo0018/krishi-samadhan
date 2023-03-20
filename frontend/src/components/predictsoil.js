import React, { useState } from 'react'
import CropItem from './cropItem';

const Predictsoil =  () => {
  let li = []
  const [crop, setData] = useState(li);
  try {
    (async()=>{
      const apicall = await fetch(`...`, {
        method: 'POST',
        headers: {
          "Content-Type": "application/json"
        }, body: JSON.stringify({}),
      })
      let data = await apicall.json()
      data = Array.from(data)
      setData(li.concat(data))
    })();
  } catch (error) {
    
  }



  return (
    <div>predictsoil
      {/* create form  */}

      {crop.map((crop) => {
        return <CropItem crops={crop} />
      })}
    </div>

  )
}

export default Predictsoil