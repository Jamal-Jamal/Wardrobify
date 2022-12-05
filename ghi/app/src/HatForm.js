import React from 'react';

class HatForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            fabric: '',
            style: '',
            color: '',
            picture_url: '',
            location: '',
            locations: [],
          };
        this.handleFabricChange = this.handleFabricChange.bind(this);
        this.handleStyleChange = this.handleStyleChange.bind(this);
        this.handleColorChange = this.handleColorChange.bind(this);
        this.handlePictureUrlChange = this.handlePictureUrlChange.bind(this);
        this.handleLocationChange = this.handleLocationChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    handleFabricChange(event) {
        const value = event.target.value;
        this.setState({ fabric: value });
        }

    handleStyleChange(event) {
        const value = event.target.value;
        this.setState({ style: value });
        }

    handleColorChange(event) {
        const value = event.target.value;
        this.setState({ color: value });
        }

    handlePictureUrlChange(event) {
        const value = event.target.value;
        this.setState({ picture_url: value });
        }

    handleLocationChange(event) {
        const value = event.target.value;
        this.setState({ location: value });
        }

    async handleSubmit(event) {
        event.preventDefault();
        const data = {...this.state};
        delete data.locations;


        const locationUrl = 'http://localhost:8090/api/hats/';
        const fetchConfig = {
          method: "post",
          body: JSON.stringify(data),
          headers: {
            'Content-Type': 'application/json',
          },
        };
        const response = await fetch(locationUrl, fetchConfig);

        if (response.ok) {
            const newHat = await response.json();
            console.log(newHat);

            this.setState({
                fabric: '',
                style: '',
                color: '',
                picture_url: '',
                location: '',
            });
          }
        }
    async componentDidMount() {
        const url = 'http://localhost:8100/api/locations/';

        const response = await fetch(url);

        if (response.ok) {
            const data = await response.json();
            this.setState({locations: data.locations});

        }
    }
    render() {
        return (
          <div className="row">
            <div className="offset-3 col-6">
              <div className="shadow p-4 mt-4">
                <h1>Add New Hat</h1>
                <form onSubmit={this.handleSubmit} id="create-hat-form">
                  <div className="form-floating mb-3">
                    <input onChange={this.handleFabricChange} placeholder="Fabric" required
                          type="text" name="fabric" id="fabric"
                          className="form-control"
                          value={this.state.name}/>
                    <label htmlFor="name">Fabric</label>
                  </div>
                  <div className="form-floating mb-3">
                    <input onChange={this.handleStyleChange}placeholder="Style" required
                          type="text" name="style" id="style"
                          className="form-control"
                          value={this.state.style}/>
                    <label htmlFor="room_count">Style</label>
                  </div>
                  <div className="form-floating mb-3">
                    <input onChange={this.handleColorChange}placeholder="Color" required
                          type="text" name="color" id="color"
                          className="form-control"
                          value={this.state.color}/>
                    <label htmlFor="color">Color</label>
                  </div>
                  <div className="form-floating mb-3">
                    <input onChange={this.handlePictureUrlChange}placeholder="Picture_Url" required
                          type="url" name="picture_url" id="picture_url"
                          className="form-control"
                          value={this.state.picture_url}/>
                    <label htmlFor="picture_url">Picture</label>
                  </div>
                  <select onChange={this.handleLocationChange}required
                        name="location" id="location"
                        className="form-select"
                        value={this.state.location}>
                    <option value="">Choose Location</option>
                    {this.state.locations.map(location => {
                        return (
                            <option key={location.href} value={location.id}>
                              {location.closet_name}
                            </option>
                        );
                    })}
                </select>
                  <button className="btn btn-primary">Add</button>
                </form>
              </div>
            </div>
          </div>
        );
      }
    }

  export default HatForm;
