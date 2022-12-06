import React, {
    useState,
    useEffect
} from 'react';
import { Link } from 'react-router-dom'

function ShoeList() {
    const [shoes, setShoes] = useState([]);
    const getShoes = async () => {
        const shoesUrl = `http://localhost:8080/api/shoes/`;
        const response = await fetch(shoesUrl);
        if (response.ok) {
            const listShoes = await response.json();
            setShoes(listShoes.shoes);
            console.log(listShoes)
        }
    };

    useEffect(() => {
        getShoes();
    }, []);

    const deleteShoe = (id) => async () => {
        try {
            const url = `http://localhost:8080/api/shoes/${id}/`;
            const deleteResponse = await fetch(url,
                {
                    method: "delete"
                }
            );

            if (deleteResponse.ok) {
                const reloadUrl = `http://localhost:8080/api/shoes/`;
                const reloadResponse = await fetch(reloadUrl);
                const newShoes = await reloadResponse.json();
                setShoes(newShoes.shoes);
            }
        }
        catch (err) {

        }
    };
    if (shoes === undefined) {
        return null;
    }
    return (
        <>
        <table className="table table-striped">
            <thead>
                <tr>
                    <th>Manufacturer</th>
                    <th>Model Name</th>
                    <th>Color</th>
                    <th>Picture</th>
                    <th>Bin</th>
                    <th>Delete</th>
                </tr>
            </thead>
            <tbody>
                {shoes.map((shoe) =>{
                    return (
                    <tr key={shoe.id}>
                        <td>{ shoe.manufacturer }</td>
                        <td>{ shoe.model_name }</td>
                        <td>{ shoe.color }</td>
                        <td><img src={ shoe.picture_url } /></td>
                        <td>{shoe.bin.bin_number}</td>
                        <td><button onClick={deleteShoe(shoe.id)} className="button">Delete</button></td>
                    </tr>
                    );
                })}
            </tbody>
        </table>
        <div className="d-grid gap-2 d-sm-flex justify-content-sm-center">
          <Link to="/shoes/new" className="btn btn-primary btn-lg px-4 gap-3">Create a new shoe</Link>
        </div>
        </>
    );
}

export default ShoeList
