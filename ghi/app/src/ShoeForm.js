import React from 'react';

class ShoesForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            manufacturer: '',
            model_name: '',
            picture_url: '',
            color: '',
            bin: '',
            bins: [],
         };

        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleManufacturerChange = this.handleManufacturerChange.bind(this);
        this.handleModelNameChange = this.handleModelNameChange.bind(this);
        this.handleColorChange = this.handleColorChange.bind(this);
        this.handlePictureUrlChange = this.handlePictureUrlChange.bind(this);
        this.handleBinChange = this.handleBinChange.bind(this);
    }

    async handleSubmit(event) {
        event.preventDefault();
        const data = { ...this.state };
        delete data.bins;
        console.log(data);

        const shoesUrl = 'http://localhost:8080/api/shoes/';
        const fetchConfig = {
            method: "post",
            body: JSON.stringify(data),
            headers: {
                'Content-Type': 'application/json',
            },
        };
        const response = await fetch(shoesUrl, fetchConfig);
        if (response.ok) {
          const newShoe = await response.json();
          console.log(newShoe);

          const cleared={
            manufacturer: '',
            model_name: '',
            picture_url: '',
            color: '',
            bin: '',
          };
          this.setState(cleared);
        }
    }

    handleManufacturerChange(event) {
        const value = event.target.value;
        this.setState({ manufacturer: value });
    }

    handleModelNameChange(event) {
        const value = event.target.value;
        this.setState({ model_name: value });
    }

    handleColorChange(event) {
        const value = event.target.value;
        this.setState({ color: value });
    }

    handlePictureUrlChange(event) {
        const value = event.target.value;
        this.setState({ picture_url: value });
    }

    handleBinChange(event) {
        const value = event.target.value;
        this.setState({ bin: value});
    }

    async componentDidMount() {
        const url = 'http://localhost:8100/api/bins/';
        const response = await fetch(url);
        if (response.ok) {
            const data = await response.json()
            this.setState({bins: data.bins});
        }
    }

    render() {
        return (
            <div className="row">
            <div className="offset-3 col-6">
                <div className="shadow p-4 mt-4">
                    <h1>Create new shoes</h1>
                    <form onSubmit={this.handleSubmit} id="create-shoes-form">
                        <div className="form-floating mb-3">
                            <input onChange={this.handleManufacturerChange}
                                value={this.state.manufacturer}
                                placeholder="Manfacturer"
                                required type="text"
                                name="manufacturer"
                                id="manufacturer"
                                className="form-control"/>
                            <label htmlFor="manufacturer">Manufacturer</label>
                        </div>
                        <div className="form-floating mb-3">
                            <input onChange={this.handleModelNameChange}
                                value={this.state.model_name}
                                placeholder="Model"
                                required type="text"
                                name="model"
                                id="model"
                                className="form-control"/>
                            <label htmlFor="name">Model name</label>
                        </div>
                        <div className="form-floating mb-3">
                            <input onChange={this.handleColorChange}
                                value={this.state.color}
                                placeholder="Color"
                                required type="text"
                                name="color"
                                id="color"
                                className="form-control"/>
                            <label htmlFor="color">Color</label>
                        </div>
                        <div className="form-floating mb-3">
                            <input onChange={this.handlePictureUrlChange}
                                value={this.state.picture_url}
                                placeholder="Picture Url"
                                type="url"
                                name="picture url"
                                id="picture url"
                                className="form-control"/>
                            <label htmlFor="picture_url">Picture Url</label>
                        </div>
                        <div className="mb-3">
                            <select onChange={this.handleBinChange}
                                value={this.state.bin}
                                required name="bin"
                                id="bin"
                                className="form-select">
                                <option value="">Choose a bin</option>
                                {this.state.bins.map(bin => {
                                    return (
                                        <option key={bin.href} value={bin.id}>
                                            {bin.bin_number} - {bin.closet_name} - {bin.bin_size}
                                        </option>
                                    )
                                })}
                            </select>
                        </div>
                        <button className="btn btn-primary">Create</button>
                    </form>
                </div>
            </div>
        </div>
        );
    }
}

export default ShoesForm;
