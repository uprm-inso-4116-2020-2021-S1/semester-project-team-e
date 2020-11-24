import React from 'react'
import {Navbar, Container} from 'react-bootstrap'

function Footer() {
    return (
        <div className="fixed-bottom">
            <Navbar bg="dark" variant="dark">
                <Container className="justify-content-md-center">
                    <Navbar.Text>
                        Footer
                    </Navbar.Text>
                </Container>
            </Navbar>
        </div>
    )
}

export default Footer
