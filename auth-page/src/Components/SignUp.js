import React, {useState} from 'react'
import {Form, Button, Card} from 'react-bootstrap'

import {Link} from 'react-router-dom'

function SignUp() {

const [email, setEmail] = useState('')
const [password, setPassword] = useState('')
const [confirmpassword, setConfirmPassword] = useState('')

const handleSubmit = (e) => {
    console.log("WORKS!")
    console.log(email)
    console.log(password)
    e.preventDefault()
}

  return (

    <>

    <Card>
        <Card.Body>
            <h2 className = "text-center mb-4 "> Sign Up</h2>
            <Form>
                <Form.Group id = "email">
                    <Form.Label>Email</Form.Label>
                    <Form.Control 
                    type = "email" 
                    placeholder='Email'  
                    value = {email} 
                    name = "email" 
                    onChange = {(e)=> {setEmail(e.target.value)}}
                    
                    />
                </Form.Group>

                <Form.Group id = "password">
                    <Form.Label>Password</Form.Label>
                    <Form.Control 
                    type = "password" 
                    placeholder='Password'  
                    value = {password}  
                    name = "password"
                    onChange = {(e)=> {setPassword(e.target.value)}}
                    
                    />
                </Form.Group>

                <Form.Group id = "passwordconfirm">
                    <Form.Label>Password Confirmation</Form.Label>
                    <Form.Control 
                    type = "password" 
                    placeholder=' Confirm Password'  
                    value = {confirmpassword} 
                    name = "confirmpassword" 
                    onChange = {(e)=> {setConfirmPassword(e.target.value)}}
                    
                    />
                </Form.Group>
                <br/>
                <Button onClick = {handleSubmit} className = "w-100" type  = "submit" >Sign Up</Button>
            </Form>
        </Card.Body>
    </Card>

    <div className = "w-100 text-center mt-2">
        Already have an account? <Link to="/login">Log In</Link>
    </div>

    
    </>
    
  )
}

export default SignUp