import { useState, ChangeEvent, FormEvent } from "react"
import { useRouter } from "next/navigation"
import { useRegisterMutation } from "@/app/redux/features/authApiSlice"
import  {toast } from 'react-toastify'

export default function useregister(){
    const router = useRouter()
    const [register,{isLoading,error:registerError}] = useRegisterMutation()
   
    const [formData, setFormData] = useState({
        first_name:'',
        last_name: '',
        email:'',
        password:'',
        re_password:'',
    })
    const {first_name, last_name, email, password, re_password} = formData

    const onChange = (event: ChangeEvent<HTMLInputElement>) => {
        const {name, value} = event.target
        setFormData({...formData,[name]:value})
    }
////  Andres Tulcan
    const onSubmit = (event:FormEvent<HTMLFormElement>) =>{
        event.preventDefault();
        register({email,first_name, last_name,  password, re_password})
       
        .unwrap()
        .then(()=>{
            toast.success('Verifique el emial')
            router.push('/auth/login')
        })
        .catch(()=>{
            toast.error('algo sale mal')
           

        })
    }
    return{
        email,
        first_name, 
        last_name,  
        password, 
        re_password,
        isLoading,
        onChange,
        onSubmit
    }
}