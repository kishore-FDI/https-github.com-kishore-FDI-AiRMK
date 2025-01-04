import {subjectCodes} from "./data.json"
const Settings = ({sub,setSub}: {sub: string, setSub: (sub: string) => void}) => {

  return (
    <section className='flex flex-col justify-between h-[100vh] max-w-[15rem] text-center py-6'>
        <h1>
            Thank You for using our site
        </h1>
        <form>
            <select value={sub} onChange={(e) => setSub(e.target.value)}>
                {subjectCodes.map((item,index)=>{
                    return(
                        <option value={item.subjectCode} key={index} title={item.title}>{item.subjectCode}</option>
                    )
                })}
            </select>
        </form>
        <h6 className='text-sm flex text-start justify-start'>
        &#x26A0;Note that this site is currently under developement and testing so in case of an issue please contact the team
        </h6>
    </section>
  )
}

export default Settings
